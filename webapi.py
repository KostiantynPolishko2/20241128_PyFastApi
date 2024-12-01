from fastapi import FastAPI, APIRouter

def create_app(title: str, router: APIRouter)->FastAPI:
    return FastAPI(
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