import os

VERSION = "1.0.0"

EMBEDDING_MODEL = "moka-ai/m3e-large"

embedding_model_dict = {
    "moka-ai/m3e-large": "/home/admin/model/downloads/moka-ai_m3e-large",
}

DEVICE = "cuda"

KB_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "knowledge_base")

EXAMPLES_ROOT_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "example")

# 缓存向量库数量
CACHED_VS_NUM = 1

SCORE_THRESHOLD = 1

# 知识库匹配向量数量
VECTOR_SEARCH_TOP_K = 1