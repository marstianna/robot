from abc import abstractmethod, ABC

from gensim import matutils
import gensim.downloader as api
from gensim.models import Doc2Vec
from gensim.models.doc2vec import TaggedDocument

import numpy as np
from langchain.embeddings.base import Embeddings
from langchain.schema import Document


class SimilarityAlgorithm(ABC):
    embeddings: Embeddings

    def __init__(self, embeddings: Embeddings):
        self.embeddings = embeddings

    @abstractmethod
    def calculate(self, origin_text: str, target_text: str) -> float:
        """calculate this algorithm"""


class CosineAlgorithm(SimilarityAlgorithm):
    def __init__(self, embeddings: Embeddings):
        super().__init__(embeddings)

    def calculate(self, origin_text: str, target_text: str) -> float:
        array1 = np.array(self.embeddings.embed_query(origin_text))
        array2 = np.array(self.embeddings.embed_query(target_text))

        cos_sim = array1.dot(array2) / (np.linalg.norm(array1) * np.linalg.norm(array2))

        return cos_sim


class Word2VecAlgorithm(SimilarityAlgorithm):

    def calculate(self, origin_text: str, target_text: str) -> float:
        model = api.load("word2vec-google-news-300")
        tokens1 = origin_text.split()
        tokens2 = target_text.split()
        vec1 = np.mean([model[token] for token in tokens1 if token in model], axis=0)
        vec2 = np.mean([model[token] for token in tokens2 if token in model], axis=0)
        return matutils.cossim(vec1, vec2)


