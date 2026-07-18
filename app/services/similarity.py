from sentence_transformers import util


def calculate_similarity(resume_embedding, jd_embedding):
    similarity = util.cos_sim(resume_embedding, jd_embedding)
    return similarity.item() * 100