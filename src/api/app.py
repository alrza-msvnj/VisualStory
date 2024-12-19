import uvicorn
from fastapi import FastAPI
from src.api.controllers.user_controller import UserController

app = FastAPI(title='VisualStory API', version='1.0')


@app.get('/')
def root():
    return {'message': 'Welcome to VisualStory!'}


app.include_router(UserController().router, prefix='/api', tags=['Users'])

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
