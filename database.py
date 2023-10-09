import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# логин и пароль для подключения к БД по требованию
SQLALCHEMY_DATABASE_URL = "postgresql://{login}:{password}.lab.karpov.courses:6432/startml"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_size=100, max_overflow=100)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    with SessionLocal() as db:
        return db


def batch_load_sql(query: str) -> pd.DataFrame:
    chunk_size = 200000
    engine = create_engine(
        "postgresql://{login}:{password}"
        "postgres.lab.karpov.courses:6432/startml"
    )
    conn = engine.connect().execution_options(stream_results=True)
    chunks = []

    for chunk_dataframe in pd.read_sql(query, conn, chunksize=chunk_size):
        chunks.append(chunk_dataframe)
    conn.close()

    return pd.concat(chunks, ignore_index=True)
