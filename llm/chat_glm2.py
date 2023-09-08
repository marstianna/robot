from typing import Optional, List

from langchain.llms.base import LLM
from langchain.llms.utils import enforce_stop_tokens
from transformers import AutoTokenizer, AutoModel


class ChatGLM2(LLM):
    max_token: int = 4096
    temperature: float = 0.8
    top_p = 0.9
    tokenizer: object = None
    model: object = None
    history = []

    def __init__(self):
        super().__init__()

    @property
    def _llm_type(self) -> str:
        return "ChatGLM2-6B"

    # 定义load_model方法，进行模型的加载
    def load_model(self):
        self.tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b",trust_remote_code=True)
        self.model = AutoModel.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True).float().cuda()

    # 实现_call方法，进行模型的推理
    def _call(self,prompt:str, stop: Optional[List[str]] = None) -> str:
        response, _ = self.model.chat(
                    self.tokenizer,
                    prompt,
                    history=self.history,
                    max_length=self.max_token,
                    temperature=self.temperature,
                    top_p=self.top_p)
        if stop is not None:
            response = enforce_stop_tokens(response, stop)
        self.history = self.history + [[None, response]]
        return response