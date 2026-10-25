from dotenv import load_dotenv

load_dotenv()
import os

for k in ['OPENAI_API_KEY','GROQ_API_KEY','OPENAI_BASE_URL','GROQ_BASE_URL']:
    v = os.getenv(k)
    print(k, 'SET' if v else 'NOT_SET')
