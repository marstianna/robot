from langchain.embeddings.huggingface import HuggingFaceEmbeddings

import config

embeddings = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL,model_kwargs={'device': config.DEVICE})

if __name__ == "__main__":
    print(embeddings.embed_documents(["LAZADA主要运营的国家为东南亚6个国家，分别为：新加坡(国家代号为SG),马来西亚(国家代号为MY),越南(国家代号为VN),菲律宾(国家代号为PH),泰国(国家代号为TH),印度尼西亚(国家代号为ID)简称印尼",
    "LAZADA的部署形式为：SG,MY,VN,PH,TH这5个国家合并部署在新加坡机房包含新加坡云上机房(机房为os30,单元为rg_sg)和新加坡云下机房(机房为sg52,单元为lazada_sg_2),ID单>独部署在印尼机房包含印尼云上机房(机房为id137,单元为rg_id)和印尼云下机房(机房为id35,单元为lazada_id)"]))
    print(embeddings.embed_query(text="新加坡的国家代号"))