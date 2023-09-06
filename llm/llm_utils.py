from langchain.chat_models import ChatOpenAI
from langchain.callbacks import AsyncIteratorCallbackHandler
from transformers import AutoTokenizer, AutoModel
import datetime
import torch

import config

tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True).cuda()

model.eval()

def call(prompt: str,max_length=2048,top_p=0.7,temperature=0.95,top_k=1):
    response, history = model.chat(tokenizer,
                                   prompt,
                                   max_length=max_length if max_length else 2048,
                                   top_p=top_p if top_p else 0.7,
                                   top_k=top_k if top_k else 1,
                                   temperature=temperature if temperature else 0.95)
    now = datetime.datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    answer = {
        "response": response,
        "status": 200,
        "time": time
    }
    log = "[" + time + "] " + '", prompt:"' + prompt + '", response:"' + repr(response) + '"'
    print(log)
    torch_gc()
    return answer


def torch_gc():
    if torch.cuda.is_available():
        with torch.cuda.device(config.DEVICE):
            torch.cuda.empty_cache()
            torch.cuda.ipc_collect()
