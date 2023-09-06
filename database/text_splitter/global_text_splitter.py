import json
from typing import Sequence, Any, List, Optional

from langchain.schema import Document
from langchain.text_splitter import TextSplitter


class FactorTextSplitter(TextSplitter):
    def split_text(self, text: str) -> List[str]:
        loads = json.loads(text)
        print(type(loads))
        if type(loads) is not list:
            #TODO ERROR
            raise TypeError("input json string is not a list type")
        return loads

    # def create_documents(
    #         self, texts: List[str], metadatas: Optional[List[dict]] = None
    #     ) -> List[Document]:
    #     docs = [Document(page_content=text, metadata={}) for text in texts]

