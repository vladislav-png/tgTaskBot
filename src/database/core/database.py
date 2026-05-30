from config import db_url_schema
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

async_engine = create_async_engine(url=db_url_schema.database_url, echo=False)

async_session_factory = async_sessionmaker(
    bind=async_engine, class_=AsyncSession, expire_on_commit=False
)


class Base(DeclarativeBase):
    def __repr__(self) -> str:
        cols = []
        for col in self.__table__.columns.keys():
            cols.append(f"{col}={getattr(self, col)}")
        return f"{self.__class__.__name__}({', '.join(cols)})"
