import database.vector_store_utils
import knowledge_base.basic_knowledge

if __name__ == "__main__":
    vector_store = database.vector_store_utils.load_vector_store(
        knowledge_base_name=knowledge_base.basic_knowledge.basic_knowledge_name)
    score = vector_store.similarity_search_with_score("SG", k=3, score_threshold=1)
    print(score)

