import uvicorn
from controllers.program_routers import router
from webapi import create_app

if __name__ == '__main__':
    uvicorn.run(create_app('Notes', router), host='127.0.0.3', port=8081)