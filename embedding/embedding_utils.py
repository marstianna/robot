import os
from functools import lru_cache

from langchain.embeddings.base import Embeddings
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

import config


@lru_cache(1)
def get_embeddings() -> Embeddings:
    local_path = config.embedding_model_dict.get(config.EMBEDDING_MODEL)
    if os.path.exists(local_path):
        return HuggingFaceEmbeddings(model_name=local_path, model_kwargs={'device': config.DEVICE})

    return HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL, model_kwargs={'device': config.DEVICE})

