from sentence_transformers import SentenceTransformer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

skills_df = pd.read_csv('skills.csv')
skills_list = skills_df['skill'].tolist()

model = SentenceTransformer('all-MiniLM-L6-v2')

skills_embeddings = model.encode(skills_list)

def semantic_match(text,skills_list=skills_list,skill_embeddings=skills_embeddings,threshold=0.8):
  text_embedding = model.encode([text])[0]

  matched_skills = []

  for skill,skill_emb in zip(skills_list,skill_embeddings):
    similarity = cosine_similarity([text_embedding],[skill_emb])[0][0]
    if similarity >= threshold:
      matched_skills.append(skill)
  
  return matched_skills