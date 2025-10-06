from fastapi import FastAPI, File, UploadFile
from extract_text import extract_text_from_file
from skills_pipeline import extract_skills
from semantic_skills import semantic_match,skills_df
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",  # your frontend URL
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # allow this origin
    allow_credentials=True,
    allow_methods=["*"],    # allow all methods (GET, POST, etc.)
    allow_headers=["*"],    # allow all headers
)

@app.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_file(file.filename, contents)

    exact_skills = extract_skills(text)
    semantic_skills = semantic_match(text)

    all_skills = set([s for s, c in exact_skills] + semantic_skills)
    all_skills_with_cat = []

    for skill in all_skills:
        cat = skills_df.set_index("skill")["category"].get(skill, "Other")

        # if string, make it a list
        if isinstance(cat, str):
            cat = [cat]
        # if Series or list, remove duplicates
        elif hasattr(cat, "tolist"):
            cat = list(set(cat.tolist()))
        elif isinstance(cat, list):
            cat = list(set(cat))

        all_skills_with_cat.append({"skill": skill, "category": cat})

    return {"skills": all_skills_with_cat}



def format_categories(cat):
    if isinstance(cat, list):
        # remove duplicates
        return list(set(cat))
    elif isinstance(cat, str):
        return [cat]
    else:
        return ["Other"]


# text = extract_text_from_file("./resumes/data/data/INFORMATION-TECHNOLOGY/13385306.pdf")
# exact_skills = extract_skills(text)
# semantic_skills = semantic_match(text)

# all_skills = set([s for s,c in exact_skills] + semantic_skills)
# all_skills_with_cat = [(s,skills_df.set_index("skill")["category"].get(s,"Other")) for s in all_skills]

# print(all_skills_with_cat)