# main.py
from fastapi import FastAPI
import uvicorn
from config.settings import APP_NAME, VERSION
from features.auth.controllers import router as auth_router

# Inisialisasi Aplikasi FastAPI
app = FastAPI(
    title=APP_NAME,
    version=VERSION,
    description="API Modular Scalable dalam Python"
)

# Root Endpoint untuk Health Check
@app.get("/")
def root():
    return {"status": "online", "app": APP_NAME, "version": VERSION}

# Register Router dari Fitur (Tinggal tambah router baru di sini jika ada fitur baru)
app.include_router(auth_router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)