from .config import BaseEnv
from functools import lru_cache
from fastapi.middleware.trustedhost import TrustedHostMiddleware
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware



@lru_cache
def get_config() -> BaseEnv:
    return BaseEnv()


DEBUG = True

ORIGINS = ["*"]

HEADERS = [
    "Accept-Encoding","Accept-Patch",
    "Access-Control-Allow-Credentials",
    "Access-Control-Allow-Header",
    "Access-Control-Allow-Methods",
    "Access-Control-Allow-Origin",
    "Authorization","Connection",
    "Content-Length","Content-Location",
    "Cookie","Host","Location",
    "Proxy-Authentication","Set-Cookie",
    "X-Content-Type-Options","X-Frame-Options",
    "X-XSS-Protection"
]

CREDENTIALS = True

METHODS = ['POST'] 

PORT = 8000

ALLOWED_HOSTS = ['*']

HOST = 'localhost'