from database.text_splitter.ali_text_splitter import AliTextSplitter
from example.example_service import DocumentWithScore


async def damo_text_split(origin_text: str) -> list[str]:
    splitter = AliTextSplitter()
    return splitter.split_text(origin_text)


async def get_knowledge_classification(classifications: str, origin_text: str) -> str:
    pass


async def extract_core_info(extract_lines: list[str], origin_text: str) -> str:
    pass


async def get_knowledge_score(max_score: int, score_rules: list[str], origin_text: str) -> str:
    pass