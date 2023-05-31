from .develop import (get_config,HEADERS,GZipMiddleware,
                      TrustedHostMiddleware,CORSMiddleware)

settings = get_config()


DEBUG_PRO = settings.DEBUG

ORIGINS_PRO = [origin for origin in settings.ORIGINS.split(',')]

HOST_PRO = settings.HOST

PORT_PRO = settings.PORT

METHODS_PRO = [method for method in settings.METHOD.split(',')]

ALLOWED_PRO = [host for host in settings.ALLOWED_HOSTS.split(',')]

CREDENTIALS_PRO = settings.CREDENTIALS