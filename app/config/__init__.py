from pydantic import BaseSettings

DEBUG_MODE=True
class DatabaseSettings(BaseSettings):
    DB_URL : str = 'mongodb+srv://user1:hung123456@cluster0.qevgiea.mongodb.net/?retryWrites=true&w=majority'
    DB_NAME: str = 'ToDo'
class Settings(DatabaseSettings):
    pass

settings = Settings()