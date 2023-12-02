from fastapi import FastAPI, Response, Request
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import segno

app = FastAPI()

app.mount("/static", StaticFiles(directory='app/static'), name='static')

templates = Jinja2Templates(directory="app/templates")


@app.post('/make_qr')
async def make_qr(url_input):
    qr_code = segno.make_qr(url_input)
    qr_code.save("./qrcodes/qr_ready.png", border=2, scale=7)
    return FileResponse(path='/Users/alexag/Desktop/qrcode_maker/qrcodes/qr_ready.png', filename='Your QR Code', media_type='multipart/form-data')


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post('/generate_qr', response_class=HTMLResponse)
async def generate_qr(request: Request, url_input):
    qr_code = segno.make_qr(url_input)
    qr_code.save("./qrcodes/qr_ready.png", border=2, scale=7)
    return templates.TemplateResponse("ready_index.html", {"request": request, "url_input": url_input})