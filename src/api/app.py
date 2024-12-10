from fastapi import FastAPI
from src.infrastructure.database import init_db

app = FastAPI(title='VisualStory API', version='1.0')

init_db()


@app.get('/')
async def read_root():
    return {'message': 'Welcome to VisualStory API'}
