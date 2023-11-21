from gensim import matutils
from  sentence_transformers import SentenceTransformer,util



if __name__ == "__main__":
    model = SentenceTransformer('/home/kidding/models/all-MiniLM-L6-v2')
    sentences = ["That is a happy person", "That is a very happy person"]
    embeddings = model.encode(sentences)
    print(util.cos_sim(embeddings[0],embeddings[1]))