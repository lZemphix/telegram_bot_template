import os
from dotenv import load_dotenv

load_dotenv()

class Settings():
	DB_HOST: str = os.getenv("DB_HOST")
	DB_PORT: int = os.getenv("DB_PORT")
	DB_USER: str = os.getenv("DB_USER")
	DB_PASS: str = os.getenv("DB_PASS")
	DB_NAME: str = os.getenv("DB_NAME")

	@property
	def DATABASE_URL_asyncpg(self):
		#postgresql+asyncpg://postgres:postgres@localhost:5432/sa
		return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
	
	@property
	def DATABASE_URL_psycopg(self):
		#postgresql+psycopg://postgres:postgres@localhost:5432/sa
		return f"postgresql+psycopg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
	
	@property
	def DATABASE_URL_sqlite(self):
		#sqlite:///users
		return f"sqlite:///{self.DB_NAME}"

settings = Settings()
