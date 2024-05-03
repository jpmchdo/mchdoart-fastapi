from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.mount("/Static", StaticFiles(directory="Static"), name="Static")

templates = Jinja2Templates(directory="Templates")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
async def index(request : Request):
    context = {"request": request}
    return templates.TemplateResponse("Index.html", context=context)
