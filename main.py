from fastapi import FastAPI, Request, Form
from instaloader import Instaloader, Post, Profile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

L = Instaloader()
app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory='htmldir')

@app.get("/")
async def root(request: Request):
    return templates.TemplateResponse("home.html", {"request":request})

@app.get("/reeldownload")
async def reeldownload(request: Request):
    return templates.TemplateResponse("reeldown.html", {"request":request})

@app.post("/submitform")
async def handle_form(request: Request,url: str = Form(...)):
    l= url.split('/')
    short_id=l[-2]
    post = Post.from_shortcode(L.context, short_id)
    L.download_post(post,target=short_id)
    return templates.TemplateResponse("s.html", {"request":request})

@app.get("/dpdownload")
async def dpdownload(request: Request):
    return templates.TemplateResponse("dpdownload.html", {"request":request})

@app.post("/submitform1")
async def handle_form1(request: Request, username: str = Form(...)):
    L.download_profile(username, profile_pic_only=True)
    return templates.TemplateResponse("s.html", {"request":request})

