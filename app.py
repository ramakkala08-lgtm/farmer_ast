from flask import Flask, request, jsonify
from flask_cors import CORS

import os
import re

from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


from langchain_google_genai import ChatGoogleGenerativeAI

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite",
    temperature=0.2
)
# =========================================================
# ENVIRONMENT
# =========================================================

app = Flask(__name__)
CORS(app)


# =========================================================
# EMBEDDING MODEL
# MUST MATCH THE MODEL USED WHEN CHROMA WAS CREATED
# =========================================================


# =========================================================
# LOAD EXISTING CHROMA DATABASE
# =========================================================




# =========================================================
# HUGGING FACE LLM
# =========================================================




# =========================================================
# DETECT NITW-SPECIFIC QUESTIONS
# ==
