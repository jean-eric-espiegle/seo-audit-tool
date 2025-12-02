import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import time


def fetch_html(url: str):
    if not url.startswith("http"):
        url = "https://" + url

    try:
        start = time.time()
        response = requests.get(url, timeout=10)
        load_time = round(time.time() - start, 2)
        return response.text, load_time
    except:
        return None, None


def get_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    common = Counter(words).most_common(10)
    return [{"keyword": w, "count": c} for w, c in common]


def audit_seo(url: str):
    html, load_time = fetch_html(url)
    if html is None:
        return {"error": "Could not fetch URL"}

    soup = BeautifulSoup(html, "html.parser")
    score = 0
    max_score = 100

    # Title
    title = soup.title.string.strip() if soup.title else None
    if title:
        score += 10
        title_length_score = 10 if 50 <= len(title) <= 60 else 5
        score += title_length_score

    # Meta Description
    meta_desc_tag = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc_tag["content"].strip() if meta_desc_tag else None
    if meta_desc:
        score += 10
        if 120 <= len(meta_desc) <= 160:
            score += 5

    # H1 tag
    h1 = soup.find("h1")
    if h1:
        score += 10
        h1_text = h1.get_text(strip=True)
    else:
        h1_text = None

    # Word count
    text = soup.get_text(" ", strip=True)
    word_count = len(text.split())
    if word_count > 300:
        score += 10

    # Keywords
    keywords = get_keywords(text)

    # Images missing alt
    images = soup.find_all("img")
    missing_alt = sum(1 for img in images if not img.get("alt"))
    if missing_alt == 0:
        score += 10

    # Viewport
    viewport = soup.find("meta", attrs={"name": "viewport"})
    has_viewport = viewport is not None
    if has_viewport:
        score += 5

    # Robots.txt
    try:
        r = requests.get(url.rstrip("/") + "/robots.txt", timeout=5)
        robots_ok = r.status_code == 200
    except:
        robots_ok = False
    if robots_ok:
        score += 5

    # Sitemap
    try:
        s = requests.get(url.rstrip("/") + "/sitemap.xml", timeout=5)
        sitemap_ok = s.status_code == 200
    except:
        sitemap_ok = False
    if sitemap_ok:
        score += 5

    # Internal & External Links
    links = soup.find_all("a")
    internal_links = 0
    external_links = 0
    for a in links:
        href = a.get("href", "")
        if href.startswith("http"):
            external_links += 1
        else:
            internal_links += 1
    if internal_links > 5:
        score += 5

    # Final score
    seo_score = int((score / max_score) * 100)

    return {
        "url": url,
        "seo_score": seo_score,
        "load_time_seconds": load_time,

        "title": title,
        "meta_description": meta_desc,
        "h1": h1_text,

        "word_count": word_count,
        "keywords": keywords,

        "missing_image_alts": missing_alt,
        "has_viewport_tag": has_viewport,
        "robots_txt_found": robots_ok,
        "sitemap_found": sitemap_ok,

        "internal_links": internal_links,
        "external_links": external_links,
    }
