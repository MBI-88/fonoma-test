from pydantic import BaseSettings

# Base configuration
class BaseEnv(BaseSettings):
    HOST: str
    PORT: int
    DEBUG:bool
    ALLOWED_HOSTS: str
    METHOD:str
    ORIGINS:str
    CREDENTIALS:bool

    class Config:
        env_file = '.env'