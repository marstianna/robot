import os

from langchain import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document


if __name__ == "__main__":
    embeddings = HuggingFaceEmbeddings(model_name="moka-ai/m3e-large", model_kwargs={'device': "cuda"})
    factors = [
        "LAZADA主要运营的国家为东南亚6个国家，分别为：新加坡,马来西亚,越南,菲律宾,泰国,印度尼西亚",
        "新加坡的国家代号为SG，线上环境部署在新加坡云上机房和新加坡云下机房",
        "马来西亚的国家代号为MY，线上环境部署在新加坡云上机房和新加坡云下机房",
        "越南的国家代号为VN，线上环境部署在新加坡云上机房和新加坡云下机房",
        "菲律宾的国家代号为PH，线上环境部署在新加坡云上机房和新加坡云下机房",
        "泰国的国家代号为TH，线上环境部署在新加坡云上机房和新加坡云下机房",
        "印度尼西亚的国家代号为ID，简称为印尼，线上环境部署在印尼云上机房和印尼云下机房",
        "新加坡云上机房的代号为os30，对应的单元为rg_sg",
        "新加坡云下机房的代号为sg52，对应的单元为lazada_sg_2",
        "印尼云上机房的代号为os30，对应的单元为rg_id",
        "印尼云下机房的代号为sg52，对应的单元为lazada_id"]
    embeddings.embed_documents(factors)

    vs_path = os.path.join(os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge_base"),
                        "multi_tenant_basic_knowledge")

    docs = [Document(page_content=text, metadata={}) for text in factors]
    faiss = FAISS.from_documents(docs, embeddings, normalize_L2=True)
    ids = [k for k, v in faiss.docstore._dict.items()]
    faiss.delete(ids)
    faiss.save_local(vs_path)
    score = faiss.similarity_search_with_score("SG", k=3, score_threshold=1)
    print(score)

