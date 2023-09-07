from functools import lru_cache

from langchain.embeddings.base import Embeddings
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

import config


@lru_cache(1)
def get_embeddings() -> Embeddings:
    return HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL, model_kwargs={'device': config.DEVICE})
