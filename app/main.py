from fastapi import FastAPI, Response
from fastapi.responses import FileResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from io import BytesIO
from starlette.responses import StreamingResponse
from PIL import Image
import segno

app = FastAPI()

app.mount("/static", StaticFiles(directory='app/static'), name='static')


@app.post('/make_qr')
async def make_qr(url_input):
    qr_code = segno.make_qr(url_input)
    qr_code.save("./qrcodes/qr_ready.png")
    return FileResponse(path='/Users/alexag/Desktop/qrcode_maker/qrcodes/qr_ready.png', filename='Your QR Code', media_type='multipart/form-data')


@app.get( "/", response_class=HTMLResponse)
async def root():
    return FileResponse("app/templates/index.html")





# @app.get("/generate_qrcode/{url}")
# def generate_qr_code(url: str):
#     qr = qrcode.QRCode(version=1, box_size=10, border=4)
#     qr.add_data(url)
#     qr.make(fit=True)
#
#     img = qr.make_image(fill="black", back_color="white")
#     img_io = BytesIO()
#     img.save(img_io, 'PNG')
#     img_io.seek(0)
#
#     return StreamingResponse(img_io, media_type="image/png")
