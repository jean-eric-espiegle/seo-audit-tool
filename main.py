from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from audit import audit_seo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/seo-audit")
def seo_audit(url: str):
    return audit_seo(url)
