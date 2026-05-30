import os

from dotenv import find_dotenv, load_dotenv
from pydantic import BaseModel, ConfigDict, Field

load_dotenv(find_dotenv())


class DatabseUrl:
    USER = os.getenv("USER")
    USER_PASS = os.getenv("USER_PASS")
    HOST = os.getenv("HOST")
    PORT = int(os.getenv("PORT"))
    DB_NAME = os.getenv("DB_NAME")


class SchemasDatabaseUrl(BaseModel):
    user: str
    user_pass: str
    host: str
    port: int = Field(gt=0)
    db_name: str

    model_config = ConfigDict(from_attributes=True, extra="forbid")

    @property
    def database_url(self) -> str:
        return f"postgresql+asyncpg://{self.user}:{self.user_pass}@{self.host}:{self.port}/{self.db_name}"


env_db_url = DatabseUrl()
db_url_schema = SchemasDatabaseUrl(
    user=env_db_url.USER,
    user_pass=env_db_url.USER_PASS,
    host=env_db_url.HOST,
    port=env_db_url.PORT,
    db_name=env_db_url.DB_NAME,
)
