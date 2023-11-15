from langchain import PromptTemplate, FAISS
from langchain.schema import Document

from embedding import embedding_utils
from example.example_service import DocumentWithScore
from llm import llm_utils
from similarity.similarity_algorithm import CosineAlgorithm, Word2VecAlgorithm


async def generate_similar_basic_knowledge(text: str, threshold_score: float = 0.65, generate_size: int = 10) -> list[
    dict]:
    template = PromptTemplate(input_variables=["input", "size"],
                              template="请根据以下内容：\n\"\"\"\n{input}\n\"\"\"\n生成意思相近的{size}条内容")
    call = llm_utils.call(prompt=template.format(input=text, size=generate_size))
    response_ = call['response']
    split = response_.split("\n")
    docs = [Document(page_content=text, metadata={}) for text in split]
    faiss = FAISS.from_documents(docs, embedding_utils.get_embeddings(), normalize_L2=True)
    origin_docs = faiss.similarity_search_with_score(text, k=generate_size, score_threshold=threshold_score)
    results = []
    for x in origin_docs:
        tmp = {}
        tmp.update({"text": x[0].page_content})
        tmp.update({"score": float(x[1])})
        results.append(tmp)
    print(results)
    return results


async def generate_similar_basic_knowledge2(text: str, threshold_score: float = 1, generate_size: int = 10) -> list[
    dict]:
    template = PromptTemplate(input_variables=["input", "size"],
                              template="请根据以下内容：\n\"\"\"\n{input}\n\"\"\"\n生成意思相近的{size}条内容")
    call = llm_utils.call(prompt=template.format(input=text, size=generate_size))
    response_ = call['response']
    split = response_.split("\n")
    similarity_algorithm = CosineAlgorithm(embedding_utils.get_embeddings())
    results = []
    for x in split:
        score = similarity_algorithm.calculate(text, x)
        if score < 1:
            tmp = {}
            tmp.update({"text": x})
            tmp.update({"score": float(score)})
            results.append(tmp)

    print(results)
    return results


async def generate_similar_basic_knowledge3(text: str, threshold_score: float = 1, generate_size: int = 10) -> list[
    dict]:
    template = PromptTemplate(input_variables=["input", "size"],
                              template="请根据以下内容：\n\"\"\"\n{input}\n\"\"\"\n生成意思相近的{size}条内容")
    call = llm_utils.call(prompt=template.format(input=text, size=generate_size))
    response_ = call['response']
    split = response_.split("\n")
    similarity_algorithm = Word2VecAlgorithm(embedding_utils.get_embeddings())
    results = []
    for x in split:
        score = similarity_algorithm.calculate(text, x)
        if score < 1:
            tmp = {}
            tmp.update({"text": x})
            tmp.update({"score": float(score)})
            results.append(tmp)

    print(results)
    return results

async def generate_similar_fine_tuning_prompt(text: str, threshold_score: float = 0.65, generate_size: int = 10) -> \
list[dict]:

    # 1.根据入参生成问题
    # 2.根据问题生成相似的问题
    question_template = PromptTemplate(input_variables=["input"],
                                       template="请根据以下内容：\n\"\"\"\n{input}\n\"\"\"\n生成对应的问题")
    call = llm_utils.call(prompt=question_template.format(input=text))
    questions_response = call['response']

    template = PromptTemplate(input_variables=["input", "size"],
                              template="请根据以下内容：\n\"\"\"\n{input}\n\"\"\"\n生成意思相近的{size}条内容")
    # generate prompt similar texts
    call = llm_utils.call(prompt=template.format(input=text, size=generate_size))
    prompt = call['response']
    split_prompt = prompt.split("\n")
    docs_prompt = [Document(page_content=text, metadata={}) for text in split_prompt]
    faiss_prompt = FAISS.from_documents(docs_prompt, embedding_utils.get_embeddings(), normalize_L2=True)
    origin_docs_prompt = faiss_prompt.similarity_search_with_score(text, k=generate_size,
                                                                   score_threshold=threshold_score)

    # generate response similar texts
    call = llm_utils.call(prompt=template.format(input=questions_response, size=generate_size))
    response = call['response']
    split_response = response.split("\n")
    docs_response = [Document(page_content=text, metadata={}) for text in split_response]
    faiss_response = FAISS.from_documents(docs_response, embedding_utils.get_embeddings(), normalize_L2=True)
    origin_docs_response = faiss_response.similarity_search_with_score(text, k=generate_size,
                                                                       score_threshold=threshold_score)

    results = []
    for x in origin_docs_prompt:
        for y in origin_docs_response:
            tmp = {}
            tmp.update({"prompt": x[0].page_content})
            tmp.update({"promptScore": float(x[1])})
            tmp.update({"response": y[0].page_content})
            tmp.update({"responseScore": float(y[1])})
            results.append(tmp)
    print(results)
    return results
