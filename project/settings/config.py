from pydantic import BaseSettings

# Base configuration
class BaseEnv(BaseSettings):
    HOST_APP: str
    PORT_APP: int
    DEBUG:bool
    ALLOWED_HOSTS: str
    METHODS:str
    ORIGINS:str
    CREDENTIALS:bool

    class Config:
        env_file = '.env'