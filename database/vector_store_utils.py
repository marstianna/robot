
from langchain import FAISS
from functools import lru_cache
from typing import List

import os

from langchain.schema import Document
from langchain.vectorstores import FAISS

import config
from embedding import embedding_utils

_VECTOR_STORE_TICKS = {}


class DocumentWithScore(Document):
    score: float = None
@lru_cache
def get_vector_store_by_name(knowledge_base_name: str) -> FAISS:
    vs_path = get_vs_path(knowledge_base_name)
    if knowledge_base_name in os.listdir(config.KB_ROOT_PATH):
        return FAISS.load_local(vs_path, embedding_utils.get_embeddings(), normalize_L2=True)
    else:
        return init_vector_store(knowledge_base_name, [Document(page_content="init", metadata={})])


def init_vector_store(knowledge_base_name: str, docs: List[Document]) -> FAISS:
    vs_path = get_vs_path(knowledge_base_name)
    faiss = FAISS.from_documents(docs, embedding_utils.get_embeddings(), normalize_L2=True)
    faiss.save_local(vs_path)
    return faiss


def search_in_vector_store(query: str,
                           top_k: int,
                           knowledge_base_name: str,
                           score_threshold: float = config.SCORE_THRESHOLD,
                           ) -> list[DocumentWithScore]:
    search_index = get_vector_store_by_name(knowledge_base_name=knowledge_base_name)

    origin_docs = search_index.similarity_search_with_score(query, k=top_k, score_threshold=score_threshold)
    docs = [DocumentWithScore(**x[0].dict(), score=x[1]) for x in origin_docs]
    return docs


def get_vs_path(knowledge_base_name: str):
    return os.path.join(config.KB_ROOT_PATH, knowledge_base_name)
