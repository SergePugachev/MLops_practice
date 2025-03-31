from fastapi import FastAPI
import uvicorn
from models.user import User

app = FastAPI()

@app.get('/')
def index():
    user_test = User(user_id='1', mail='itmo@itmo.com', password='qwerty')
    return 'Hello ' + user_test.role

if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8080, reload=True)