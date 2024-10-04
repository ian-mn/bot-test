from pydantic import SecretStr
from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    token: SecretStr

    class Config:
        env_file = ".env"
        extra = "ignore"


settings = BotSettings()
