from functools import lru_cache

from langchain.chat_models import ChatOpenAI
from langchain.callbacks import AsyncIteratorCallbackHandler
from langchain.schema import Document
from transformers import AutoTokenizer, AutoModel
import datetime
import torch

import config
import database.vector_store_utils
from knowledge_base import basic_knowledge
from llm.chat_glm2 import ChatGLM2


@lru_cache(1)
def get_llm():
    return ChatGLM2().load_model()



# def call(prompt: str, max_length=2048, top_p=0.7, temperature=0.95, top_k=1):
#     response, history = model.chat(tokenizer,
#                                    prompt,
#                                    max_length=max_length,
#                                    top_p=top_p,
#                                    top_k=top_k,
#                                    temperature=temperature)
#     now = datetime.datetime.now()
#     time = now.strftime("%Y-%m-%d %H:%M:%S")
#     answer = {
#         "response": response,
#         "status": 200,
#         "time": time
#     }
#     log = "[" + time + "] " + '", prompt:"' + prompt + '", response:"' + repr(response) + '"'
#     print(log)
#     torch_gc()
#     return answer
#
#
# def torch_gc():
#     if torch.cuda.is_available():
#         with torch.cuda.device(config.DEVICE):
#             torch.cuda.empty_cache()
#             torch.cuda.ipc_collect()
