from fastapi import FastAPI
import uvicorn as server
from api.views import router



# Api
app = FastAPI(
    debug=True,title="Fonoma Api",
    description="Api for making operations",
    version="1.0"
    )


app.include_router(router=router,tags=["solution"])


if __name__ == "__main__":
    debug = True 
    if debug:
        from project.settings.develop import (
            CORSMiddleware,ORIGINS,CREDENTIALS,METHODS,HEADERS,
            HOST,PORT,DEBUG
        )
        app.debug = DEBUG
        host = HOST
        port = PORT
        app.add_middleware(
            CORSMiddleware,allow_headers=HEADERS,
            allow_origins=ORIGINS,
            allow_credentials=CREDENTIALS,
            allow_methods=METHODS
        )
    else:
        from project.settings.production import (
            TrustedHostMiddleware,GZipMiddleware,CORSMiddleware,
            HEADERS,ORIGINS_PRO,HOST_PRO,PORT_PRO,DEBUG_PRO,ALLOWED_PRO,
            CREDENTIALS_PRO
        )

        app.debug = DEBUG_PRO
        host = HOST_PRO
        port = PORT
        app.add_middleware(
            CORSMiddleware,allow_headers=HEADERS,
            allow_origins=ORIGINS_PRO,allow_credentials=CREDENTIALS_PRO,
            allow_methods=METHODS
        )
        app.add_middleware(
            TrustedHostMiddleware,allowed_hosts=ALLOWED_PRO
        )
        app.add_middleware(
            GZipMiddleware,minimum_size=1000,
        )

    server.run("main:app",host=host,port=port,reload=True)