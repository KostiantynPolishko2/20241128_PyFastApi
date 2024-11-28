import uvicorn
from webapi import app

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.3', port=8081)