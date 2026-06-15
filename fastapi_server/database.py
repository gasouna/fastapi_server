from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from fastapi_server.settings import Settings

engine = create_engine(Settings().DATABASE_URL)


def get_session():
    with Session(engine) as session:
        yield session
