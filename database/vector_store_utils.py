from types import NoneType

from langchain import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings.base import Embeddings
from functools import lru_cache
from typing import List, Tuple

import os

from langchain.schema import Document
from langchain.vectorstores.base import VST

import config
import embedding.embedding_utils
import knowledge_base.basic_knowledge

_VECTOR_STORE_TICKS = {}

embeddings = embedding.embedding_utils.embeddings


@lru_cache
def get_vector_store_by_name(knowledge_base_name: str) -> VST:
    vs_path = get_vs_path(knowledge_base_name)
    if knowledge_base_name in os.listdir(config.KB_ROOT_PATH):
        return FAISS.load_local(vs_path, embeddings, normalize_L2=True)
    else:
        return init_vector_store(knowledge_base_name, [Document(page_content="init", metadata={})])


def init_vector_store(knowledge_base_name: str, docs: List[Document]) -> VST:
    vs_path = get_vs_path(knowledge_base_name)
    faiss = FAISS.from_documents(docs, embeddings, normalize_L2=True)
    faiss.save_local(vs_path)
    return faiss


def search_in_vector_store(query: str,
                           top_k: int,
                           knowledge_base_name: str,
                           score_threshold: float = config.SCORE_THRESHOLD,
                           ) -> list[tuple[Document, float]]:
    search_index = get_vector_store_by_name(knowledge_base_name=knowledge_base_name)
    return search_index.similarity_search_with_score(query, k=top_k, score_threshold=score_threshold)


def get_vs_path(knowledge_base_name: str):
    return os.path.join(config.KB_ROOT_PATH, knowledge_base_name)
