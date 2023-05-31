from fastapi import FastAPI
from fastapi.responses import RedirectResponse
import uvicorn


# Api
app = FastAPI(
    debug=True,title="Fonoma Api",
    description="Api for making operations",
    version="1.0"
    )



@app.get('/')
async def index() -> RedirectResponse:
    return RedirectResponse(url='/solution')



if __name__ == "__main__":
    uvicorn.run("main:app",host="localhost",port=8000,reload=True)