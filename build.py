#!/usr/bin/env python3
"""
Build script: injects real vetted listings from listings.json into index.html
"""

import json
import html
import re
from pathlib import Path

LISTINGS_JSON = Path("/Users/tonyclaw/Documents/Tony-Tasks/Tony's Vault/Projects/VA-Claims-Help-Finder/listings/listings.json")
INDEX_HTML = Path("/tmp/va-claims-site/index.html")

BADGE_CLASS_MAP = {
    "VSO": "vso",
    "Law Firm": "law",
    "Nonprofit": "nonprofit",
    "Medical Eval": "medical",
    "Education": "edu",
    "Other": "other",
}

PRICE_CLASS_MAP = {
    "Free": "price-free",
    "Contingency": "price-contingency",
}

def badge_class(listing_type):
    return BADGE_CLASS_MAP.get(listing_type, "other")

def price_class(pricing_model):
    return PRICE_CLASS_MAP.get(pricing_model, "price-paid")

def escape(text):
    return html.escape(str(text)) if text is not None else ""

def build_card(listing):
    name = escape(listing["name"])
    name_lower = listing["name"].lower()
    type_str = escape(listing["type"])
    type_lower = listing["type"].lower()
    website = escape(listing["website"])
    pricing_model = escape(listing["pricing_model"])
    review_summary = escape(listing["review_summary"])
    featured = listing.get("featured", False)

    featured_class = " listing-card-featured" if featured else ""
    featured_banner = '<div class="featured-banner">⭐ Editor\'s Pick</div>' if featured else ""

    bc = badge_class(listing["type"])
    pc = price_class(listing["pricing_model"])

    # Phone
    phone = listing.get("phone")
    if phone:
        phone_html = f'<span class="meta-phone">📞 {escape(phone)}</span>'
    else:
        phone_html = ""

    # Caveat
    caveat = listing.get("caveat")
    if caveat:
        caveat_html = f'<div class="card-caveat">⚠️ {escape(caveat)}</div>'
    else:
        caveat_html = ""

    # Accreditation
    accreditation = listing.get("accreditation", [])
    if "VA-Accredited" in accreditation:
        accreditation_html = '<span class="verified-badge">✓ VA-Accredited</span>'
    else:
        accreditation_html = '<span class="verified-badge unverified">Not VA-Accredited</span>'

    card = f'''    <div class="listing-card{featured_class}" data-name="{name_lower}" data-type="{type_lower}">
      <div class="card-header">
        <span class="card-name">{name}</span>
        <span class="badge badge-{bc}">{type_str}</span>
      </div>
      {featured_banner}
      <p class="card-desc">{review_summary}</p>
      {caveat_html}
      <div class="card-meta">
        <span class="meta-price {pc}">{pricing_model}</span>
        {phone_html}
      </div>
      <div class="card-footer">
        {accreditation_html}
        <a href="{website}" target="_blank" rel="noopener" class="btn-visit">Visit Website →</a>
      </div>
    </div>'''
    return card

def main():
    with open(LISTINGS_JSON, "r", encoding="utf-8") as f:
        listings = json.load(f)

    # Filter active only
    active = [l for l in listings if l.get("status") == "active"]

    # Sort: featured first, then by score descending
    active.sort(key=lambda l: (not l.get("featured", False), -l.get("score", 0)))

    print(f"Building cards for {len(active)} active listings...")

    cards_html = "\n\n".join(build_card(l) for l in active)

    # Read index.html
    content = INDEX_HTML.read_text(encoding="utf-8")

    # Replace listing grid content
    # Pattern: everything between <div class="listing-grid"> and </div>\n</section>
    pattern = r'(<div class="listing-grid">).*?(</div>\s*\n</section>)'
    replacement = f'\\1\n\n{cards_html}\n\n  \\2'

    new_content, count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    if count == 0:
        print("ERROR: Could not find listing-grid section in index.html")
        return 1

    # Update trust bar: change "10" Vetted Companies to "43"
    # Target: <strong>10</strong><span>Vetted Companies Listed</span>
    new_content = re.sub(
        r'<strong>10</strong>(<span>Vetted Companies Listed</span>)',
        r'<strong>43</strong>\1',
        new_content
    )

    INDEX_HTML.write_text(new_content, encoding="utf-8")
    print(f"✅ index.html updated with {len(active)} listings")
    print("✅ Trust bar updated: 10 → 43")
    return 0

if __name__ == "__main__":
    exit(main())
