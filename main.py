from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from audit import audit_seo, audit_competitor

app = FastAPI(
    title="SEO Audit API",
    description="Full in-depth SEO audit for websites + competitor analysis",
    version="2.0"
)

# Allow frontend to access the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # You can restrict later
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/seo-audit")
def seo_audit(url: str):
    """
    Full SEO audit for a single website.
    """
    return audit_seo(url)


@app.get("/seo-compare")
def seo_compare(url1: str, url2: str):
    """
    Compare two websites side-by-side.
    """
    return audit_competitor(url1, url2)
