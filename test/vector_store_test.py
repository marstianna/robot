import os

from langchain import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.schema import Document


if __name__ == "__main__":
    embeddings = HuggingFaceEmbeddings(model_name="moka-ai/m3e-large", model_kwargs={'device': "cuda"})
    factors = [
        "LAZADA主要运营的国家为东南亚6个国家，分别为：新加坡(国家代号为SG),马来西亚(国家代号为MY),越南(国家代号为VN),菲律宾(国家代号为PH),泰国(国家代号为TH),印度尼西亚(国家代号为ID)简称印尼",
        "LAZADA的部署形式为：SG,MY,VN,PH,TH这5个国家合并部署在新加坡机房包含新加坡云上机房(机房为os30,单元为rg_sg)和新加坡云下机房(机房为sg52,单元为lazada_sg_2),ID单>独部署在印尼机房包含印尼云上机房(机房为id137,单元为rg_id)和印尼云下机房(机房为id35,单元为lazada_id)"]
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

