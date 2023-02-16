from fastapi import FastAPI, Request, Form
from instaloader import Instaloader, Post, Profile
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from instagramy.plugins.download import *

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
async def handle_form(request: Request,url: str = Form(...),l_username: str = Form(...), l_password: str = Form(...)):
    l= url.split('/')
    short_id=l[-2]
    post = Post.from_shortcode(L.context, short_id)
    L.login(l_username, l_password) 
    L.download_post(post,target=short_id)
    return templates.TemplateResponse("s.html", {"request":request})

@app.get("/dpdownload")
async def dpdownload(request: Request):
    return templates.TemplateResponse("dpdownload.html", {"request":request})

@app.post("/submitform1")
async def handle_form1(request: Request, u_name: str = Form(...)):
    download_profile_pic(username=u_name)
    return templates.TemplateResponse("s.html", {"request":request})

