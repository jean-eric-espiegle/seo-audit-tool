import requests
from bs4 import BeautifulSoup
from collections import Counter
import re
import time
from urllib.parse import urljoin, urlparse


# -------------------------------------
# Helper: Fetch HTML and measure timing
# -------------------------------------
def fetch_html(url: str):
    if not url.startswith("http"):
        url = "https://" + url

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/119.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    }

    try:
        start = time.time()
        response = requests.get(url, headers=headers, timeout=12)
        load_time = round(time.time() - start, 2)
        return response.text, response, load_time
    except Exception as e:
        print("Fetch error:", e)
        return None, None, None



# -------------------------------------
# Helper: Keyword Extraction
# -------------------------------------
def get_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{4,}\b', text.lower())
    common = Counter(words).most_common(10)
    return [{"keyword": w, "count": c} for w, c in common]


# -------------------------------------
# B) Broken Link Checker
# -------------------------------------
def check_broken_links(soup, base_url):
    internal_broken = []
    external_broken = []
    internal_good = 0
    external_good = 0

    all_links = soup.find_all("a")

    for link in all_links:
        href = link.get("href")
        if not href or href.startswith("#"):
            continue

        if href.startswith("http"):
            absolute = href
        else:
            absolute = urljoin(base_url, href)

        try:
            r = requests.head(absolute, timeout=5)
            status = r.status_code
        except:
            status = None

        is_internal = urlparse(base_url).netloc in absolute

        if status and status < 400:
            if is_internal:
                internal_good += 1
            else:
                external_good += 1
        else:
            if is_internal:
                internal_broken.append(absolute)
            else:
                external_broken.append(absolute)

    return {
        "internal_good": internal_good,
        "external_good": external_good,
        "internal_broken": internal_broken,
        "external_broken": external_broken
    }


# -------------------------------------
# C) Schema / Structured Data Detection
# -------------------------------------
def detect_structured_data(soup):
    structures = []

    # JSON-LD scripts
    json_ld = soup.find_all("script", type="application/ld+json")
    for item in json_ld:
        try:
            structures.append(item.string.strip())
        except:
            pass

    # Microdata itemscope
    microdata = soup.find_all(attrs={"itemscope": True})
    if microdata:
        structures.append("Microdata: " + str(len(microdata)))

    # RDFa
    rdfa = soup.find_all(attrs={"typeof": True})
    if rdfa:
        structures.append("RDFa: " + str(len(rdfa)))

    return structures


# -------------------------------------
# D) Lighthouse-Lite Performance Metrics
# -------------------------------------
def performance_insights(response, soup):
    headers = dict(response.headers)

    # Page size
    page_size = len(response.content)

    # Script count
    script_count = len(soup.find_all("script"))

    # Image count
    image_count = len(soup.find_all("img"))

    # Total DOM nodes
    dom_nodes = len(soup.find_all())

    return {
        "page_size_bytes": page_size,
        "script_count": script_count,
        "image_count": image_count,
        "dom_nodes": dom_nodes,
        "server_headers": {
            "content_type": headers.get("Content-Type"),
            "server": headers.get("Server"),
            "cache_control": headers.get("Cache-Control"),
            "content_encoding": headers.get("Content-Encoding"),
        }
    }


# -------------------------------------
# E) Competitor Comparison Helper
# -------------------------------------
def competitor_compare(main_data, competitor_data):
    """
    Compare:
    - SEO Score
    - Word Count
    - Load Time
    - Internal Links
    - Missing Alts
    """

    return {
        "main_url": main_data["url"],
        "competitor_url": competitor_data["url"],

        "seo_score_diff": competitor_data["seo_score"] - main_data["seo_score"],
        "word_count_diff": competitor_data["word_count"] - main_data["word_count"],
        "load_time_diff": competitor_data["load_time_seconds"] - main_data["load_time_seconds"],
        "missing_alts_diff": competitor_data["missing_image_alts"] - main_data["missing_image_alts"],
        "internal_links_diff": competitor_data["internal_links"] - main_data["internal_links"],
    }


# -------------------------------------
# Main SEO Audit Function
# -------------------------------------
def audit_seo(url: str):
    html, response, load_time = fetch_html(url)
    if html is None:
        return {"error": "Could not fetch URL"}

    soup = BeautifulSoup(html, "html.parser")

    score = 0
    max_score = 100

    # Title Tag
    title = soup.title.string.strip() if soup.title else None
    if title:
        score += 10
        if 50 <= len(title) <= 60:
            score += 5

    # Meta Description
    meta_desc_tag = soup.find("meta", attrs={"name": "description"})
    meta_desc = meta_desc_tag.get("content", "").strip() if meta_desc_tag else None
    if meta_desc:
        score += 10

    # H1 Tag
    h1 = soup.find("h1")
    h1_text = h1.get_text(strip=True) if h1 else None
    if h1:
        score += 10

    # Word Count
    text = soup.get_text(" ", strip=True)
    word_count = len(text.split())
    if word_count > 300:
        score += 10

    # Keywords
    keywords = get_keywords(text)

    # Missing Alts
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
        robots = requests.get(url.rstrip("/") + "/robots.txt", timeout=5)
        robots_ok = robots.status_code == 200
    except:
        robots_ok = False
    if robots_ok:
        score += 5

    # Sitemap
    try:
        sitemap = requests.get(url.rstrip("/") + "/sitemap.xml", timeout=5)
        sitemap_ok = sitemap.status_code == 200
    except:
        sitemap_ok = False
    if sitemap_ok:
        score += 5

    # Internal vs External Links
    links = soup.find_all("a")
    internal_links = 0
    external_links = 0

    for a in links:
        href = a.get("href", "")
        if href.startswith("http"):
            external_links += 1
        else:
            internal_links += 1

    # Bonus score
    if internal_links > 5:
        score += 5

    # Broken Links
    broken = check_broken_links(soup, url)

    # Structured Data
    schema = detect_structured_data(soup)

    # Performance Insights
    perf = performance_insights(response, soup)

    seo_score = int((score / max_score) * 100)

    return {
        "url": url,
        "seo_score": seo_score,

        "title": title,
        "meta_description": meta_desc,
        "h1": h1_text,

        "word_count": word_count,
        "keywords": keywords,

        "missing_image_alts": missing_alt,
        "load_time_seconds": load_time,

        "has_viewport_tag": has_viewport,
        "robots_txt_found": robots_ok,
        "sitemap_found": sitemap_ok,

        "internal_links": internal_links,
        "external_links": external_links,

        "broken_links": broken,
        "structured_data": schema,
        "performance": perf
    }


# -------------------------------------
# Wrapper for competitor API
# -------------------------------------
def audit_competitor(url1: str, url2: str):
    data1 = audit_seo(url1)
    data2 = audit_seo(url2)

    return {
        "main": data1,
        "competitor": data2,
        "comparison": competitor_compare(data1, data2)
    }
