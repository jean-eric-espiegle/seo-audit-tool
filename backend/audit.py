import requests
from bs4 import BeautifulSoup
import time


def fetch_html(url: str):
    if not url.startswith("http"):
        url = "https://" + url
    
    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        load_time = round(time.time() - start, 2)
        return response.text, load_time
    except Exception:
        return None, None


def audit_seo(url: str):
    html, load_time = fetch_html(url)
    if html is None:
        return {"error": "Could not fetch URL"}

    soup = BeautifulSoup(html, "html.parser")
    
    # Title
    title = soup.title.string if soup.title else None

    # Meta description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc["content"] if meta_desc else None

    # H1 tag
    h1 = soup.find("h1")
    h1_text = h1.get_text(strip=True) if h1 else None

    # Word count
    text = soup.get_text(" ", strip=True)
    word_count = len(text.split())

    # Images missing alt
    images = soup.find_all("img")
    images_missing_alt = sum(1 for img in images if not img.get("alt"))

    # Mobile-friendly tag
    viewport = soup.find("meta", attrs={"name": "viewport"})
    has_viewport = viewport is not None

    # Check robots.txt
    try:
        robots = requests.get(url.rstrip("/") + "/robots.txt", timeout=5)
        robots_ok = robots.status_code == 200
    except:
        robots_ok = False

    # Check sitemap
    try:
        sitemap = requests.get(url.rstrip("/") + "/sitemap.xml", timeout=5)
        sitemap_ok = sitemap.status_code == 200
    except:
        sitemap_ok = False

    return {
        "url": url,
        "title": title,
        "meta_description": meta_desc,
        "h1": h1_text,
        
        "word_count": word_count,
        "missing_image_alts": images_missing_alt,
        "load_time_seconds": load_time,

        "has_viewport_tag": has_viewport,
        "robots_txt_found": robots_ok,
        "sitemap_found": sitemap_ok,
    }
