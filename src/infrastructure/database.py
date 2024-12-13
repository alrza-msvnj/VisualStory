from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from src.infrastructure.config import Config

DATABASE_URL = Config.SQLALCHEMY_DATABASE_URI

engine = create_async_engine(DATABASE_URL, echo=True)  # echo=True: Enables SQL query logging
session_factory = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()
