from sqlmodel import SQLModel, create_engine, Session

from app.config import settings

engine = create_engine(settings.POSTGRES_URI)
session = Session(autocommit=False, autoflush=False, bind=engine)


def init_db():
    SQLModel.metadata.create_all(engine)


def close_db():
    session.close_all()
    engine.dispose()
