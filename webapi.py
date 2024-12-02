from fastapi import FastAPI, APIRouter
from handlers.exception_handlers import *
from fastapi.exceptions import RequestValidationError

def create_app(title: str, router: APIRouter)->FastAPI:
    app = FastAPI(
        title=f'{title}Api',
              description='WebApi CRUD of Note entities',
              version='1.0.0',
              docs_url='/swagger',
              contact={
                  'name': 'itstep academy',
                  'url': 'https://itstep.dp.ua',
                  'email': 'polxs_wp31@student.itstep.org'
              },
              routes= router.routes)

    app.add_exception_handler(RequestValidationError, validation_exception_handler)
    app.add_exception_handler(HTTPException, http_exception_handler)

    return app
