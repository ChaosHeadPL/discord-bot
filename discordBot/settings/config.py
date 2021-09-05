from pydantic import BaseSettings


class Settings(BaseSettings):
    VERSION: str = "0.0.1"

    TOKEN = ""
    