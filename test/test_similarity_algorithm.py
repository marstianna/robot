from gensim import matutils
from gensim.models.doc2vec import TaggedDocument, Doc2Vec


def test(target_text):
    origin_text = "自动化会生成大量的文本任务，需要大量的人力来做标注"
    print(target_text.split())
    corpus = [TaggedDocument(origin_text.split(), ["origin_text"]),
              TaggedDocument(target_text.split(), ["target_text"])]
    model = Doc2Vec(corpus, vector_size=100, window=5, min_count=1, workers=4)
    vec1 = model.dv["origin_text"]
    dict1 = {}
    count1 = 0
    for value in vec1:
        dict1.update({count1:value})
        count1 += 1
    vec2 = model.dv["target_text"]
    dict2 = {}
    count2 = 0
    for value in vec2:
        dict2.update({count2:value})
        count2 += 1
    return matutils.cossim(dict1, dict2)

if __name__ == "__main__":
    target_texts = ["随着自动化技术的普及，生成大量文本的任务变得越来越简单，但需要投入更多的人力。","自动化可以减轻大量文本处理的工作量，但仍需耗费大量的人力。","泰国的国家代号为TH，线上环境部署在新加坡云上机房和新加坡云下机房，预发环境部署在新加坡云上预发机房和新加坡云下预发机房"]
    print([test(text) for text in target_texts])
