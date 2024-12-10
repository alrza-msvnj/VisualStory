from fastapi import FastAPI

app = FastAPI(title='VisualStory API', version='1.0')


@app.get('/')
async def read_root():
    return {'message': 'Welcome to VisualStory API'}
