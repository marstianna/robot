from langchain import FAISS, FewShotPromptTemplate, PromptTemplate, LLMChain
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.schema import Document
from transformers.pipelines import task

from langchain.prompts.example_selector import SemanticSimilarityExampleSelector

import config
from example import prompt_examples
from fastapi import Body
from knowledge_base import basic_knowledge
from embedding import embedding_utils
import json

from database import vector_store_utils

embeddings = embedding_utils.embeddings

example_selector = SemanticSimilarityExampleSelector.from_examples(prompt_examples.prompt_examples, embeddings, FAISS,
                                                                   k=config.VECTOR_SEARCH_TOP_K)


class DocumentWithScore(Document):
    score: float = None


def search_examples(query: str = Body(..., description="用户输入", examples=["你好"])):
    # 首先从基础知识库里面检索对应的基础只是
    docs = vector_store_utils.search_in_vector_store(query=query,
                                                     knowledge_base_name=basic_knowledge.basic_knowledge_name,
                                                     top_k=5)


    context = "\n".join([doc.page_content for doc in docs])

    print("search_examples:"+context)

    # 获取到根据输入匹配到的对应的examples
    examples = [example_.update({"basic_knowledge": context}) for example_ in
                example_selector.select_examples({"input": query})]

    return context,examples
