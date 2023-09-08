from functools import lru_cache

from langchain import FAISS, FewShotPromptTemplate, PromptTemplate, LLMChain
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.chat_models import ChatOpenAI
from langchain.prompts.example_selector.base import BaseExampleSelector
from langchain.schema import Document
from transformers.pipelines import task

from langchain.prompts.example_selector import SemanticSimilarityExampleSelector

import config
from example import prompt_examples
from fastapi import Body
from embedding import embedding_utils
from knowledge_base import basic_knowledge
from embedding import embedding_utils
import json

from database import vector_store_utils

class DocumentWithScore(Document):
    score: float = None


def search_examples(query: str = Body(..., description="用户输入", examples=["你好"])):
    # 首先从基础知识库里面检索对应的基础只是
    docs = vector_store_utils.search_in_vector_store(query=query,
                                                     knowledge_base_name=basic_knowledge.basic_knowledge_name,
                                                     score_threshold=1,
                                                     top_k=3)

    context = "。".join([doc.page_content for doc in docs])

    # 获取到根据输入匹配到的对应的examples
    matched_examples = get_example_selector().select_examples({"input": query})


    for example_ in matched_examples:
        example_.update({"basic_knowledge": context})

    return context,matched_examples

def add_example(example: dict):
    if not validate_example():
        raise ValueError("input example is error")
    prompt_examples.append(example)


def validate_example() -> bool:
    return True

@lru_cache(1)
def get_example_selector() -> BaseExampleSelector:
    return SemanticSimilarityExampleSelector.from_examples(prompt_examples.prompt_examples,
                                                           embedding_utils.get_embeddings(),
                                                           FAISS,
                                                           k=config.VECTOR_SEARCH_TOP_K)
