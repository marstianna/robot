from langchain.embeddings.huggingface import HuggingFaceEmbeddings

import os


if __name__ == "__main__":
    os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
    embeddings = HuggingFaceEmbeddings(model_name="/home/admin/model/downloads/moka-ai_m3e-large",model_kwargs={'device': "cuda"})
    print(embeddings.embed_documents(["新加坡的租户标为LAZADA_SG"]))
    print(embeddings.embed_query(text="新加坡的租户标"))