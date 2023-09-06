from types import NoneType

from langchain import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings.base import Embeddings
from functools import lru_cache
from typing import List

import os

from langchain.schema import Document

import config
import embedding.embedding_utils

_VECTOR_STORE_TICKS = {}


@lru_cache(config.CACHED_VS_NUM)
def load_vector_store(knowledge_base_name: str, tick: int = 0, ):
    vs_path = get_vs_path(knowledge_base_name)
    embeddings = embedding.embedding_utils.embeddings
    if not os.path.exists(vs_path):
        os.makedirs(vs_path)
    if "index.faiss" in os.listdir(vs_path):
        search_index = FAISS.load_local(vs_path, embeddings, normalize_L2=True)
    else:
        # create an empty vector store
        doc = Document(page_content="init", metadata={})
        search_index = FAISS.from_documents([doc], embeddings, normalize_L2=True)
        ids = [k for k, v in search_index.docstore._dict.items()]
        search_index.delete(ids)
        search_index.save_local(vs_path)

    if tick == 0:  # vector store is loaded first time
        _VECTOR_STORE_TICKS[knowledge_base_name] = 0

    return search_index

def search_in_vector_store(query: str,
                           top_k: int,
                           knowledge_base_name: str,
                           score_threshold: float = config.SCORE_THRESHOLD,
                           ) -> List[Document]:
    search_index = load_vector_store(knowledge_base_name = knowledge_base_name,
                                     tick=_VECTOR_STORE_TICKS.get(knowledge_base_name))
    docs = search_index.similarity_search_with_score(query, k=top_k, score_threshold=score_threshold)
    return docs

def get_vs_path(knowledge_base_name: str):
    return os.path.join(config.KB_ROOT_PATH, knowledge_base_name)
