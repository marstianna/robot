from langchain.embeddings.huggingface import HuggingFaceEmbeddings

import config

embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL,model_kwargs={'device': config.DEVICE})
