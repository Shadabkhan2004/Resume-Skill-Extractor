import spacy
from spacy.matcher import PhraseMatcher
import pandas as pd


nlp = spacy.load("en_core_web_sm")

skills_df = pd.read_csv("skills.csv").drop_duplicates(subset=["skill"])
skills = skills_df['skill'].tolist()
categories = skills_df.set_index("skill")["category"].to_dict()

matcher = PhraseMatcher(nlp.vocab,attr='LOWER')
patterns = [nlp(skill) for skill in skills]
matcher.add("SKILLS",patterns)

def extract_skills(text):
  doc = nlp(text)
  matches = matcher(doc)
  extracted = set()

  for match_id,start,end in matches:
    span = doc[start:end]
    skill = span.text
    category = categories.get(skill,"Other")
    extracted.add((skill,category))
  return list(extracted)
