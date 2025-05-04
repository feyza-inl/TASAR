from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Statik dosyaların frontend klasöründen sunulması
app.mount("/static", StaticFiles(directory="frontend"), name="static")

# Anasayfa
@app.get("/", response_class=HTMLResponse)
async def home():
    with open("frontend/tasar.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

# Hakkımızda Sayfası
@app.get("/hakkimizda", response_class=HTMLResponse)
async def hakkimizda():
    with open("frontend/hakkimizda.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

# İletişim Sayfası
@app.get("/iletisim", response_class=HTMLResponse)
async def iletisim():
    with open("frontend/iletisim.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

# Kaydol Sayfası
@app.get("/kaydol", response_class=HTMLResponse)
async def kaydol():
    with open("frontend/kaydol.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

# Ücretlendirme Sayfası
@app.get("/ucretlendirme", response_class=HTMLResponse)
async def ucretlendirme():
    with open("frontend/ucretlendirme.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())

# Giriş Sayfası
@app.get("/giris", response_class=HTMLResponse)
async def giris():
    with open("frontend/giris.html", "r", encoding="utf-8") as file:
        return HTMLResponse(content=file.read())
