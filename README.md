# Resume Skill Extractor

A simple web app that extracts and categorizes skills from resumes using **NLP**.  
Built with **FastAPI** (backend) and **React** (frontend).

---

## 🚀 Features
- Upload resumes in PDF, DOCX, or TXT format  
- Extracts and categorizes technical & soft skills  
- Displays top 10–12 relevant skills  
- Fast and lightweight setup  

---

## 🧠 Tech Stack
- **Backend:** FastAPI, spaCy, pandas  
- **Frontend:** React, Axios, Vite, Tailwind CSS  

---

## ⚙️ Setup

### Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --reload
