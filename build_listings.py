#!/usr/bin/env python3
"""Build individual listing pages for vaclaimshelp.guide"""

import json
import os
from html import escape

# Load listings
with open('listings/listings.json') as f:
    listings = json.load(f)

os.makedirs('listings', exist_ok=True)

def score_badge(score):
    if score is None:
        return ''
    try:
        s = float(score)
    except:
        return f'<span class="score-badge score-na">{escape(str(score))}</span>'
    if s >= 4.5:
        color = '#2e7d32'
        label = 'Excellent'
    elif s >= 3.5:
        color = '#b8860b'
        label = 'Good'
    else:
        color = '#8b0000'
        label = 'Mixed'
    return f'<span class="score-badge" style="background:{color};color:#fff;padding:3px 10px;border-radius:12px;font-size:.85rem;font-weight:600;">{s}/5 — {label}</span>'

def type_badge(t):
    colors = {
        'VSO': '#1565c0',
        'Legal': '#6a1b9a',
        'Medical Eval': '#00695c',
        'Nonprofit': '#e65100',
        'Educational': '#37474f',
        'Government': '#1a237e',
    }
    color = colors.get(t, '#555')
    return f'<span style="background:{color};color:#fff;padding:3px 10px;border-radius:12px;font-size:.85rem;font-weight:600;">{escape(t or "")}</span>'

def build_page(listing):
    lid = listing['id']
    name = listing.get('name', '')
    website = listing.get('website', '')
    phone = listing.get('phone', '')
    email = listing.get('email', '')
    ltype = listing.get('type', '')
    categories = listing.get('categories', [])
    service_areas = listing.get('service_areas', [])
    pricing_model = listing.get('pricing_model', '')
    accreditation = listing.get('accreditation', '')
    score = listing.get('score')
    reddit_sentiment = listing.get('reddit_sentiment', '')
    review_summary = listing.get('review_summary', '')
    caveat = listing.get('caveat', '')
    featured = listing.get('featured', False)

    service_area_str = ', '.join(service_areas) if service_areas else 'Nationwide'
    categories_html = ''.join(
        f'<span style="background:#e8eaf6;color:#283593;padding:3px 10px;border-radius:12px;font-size:.82rem;margin:2px 2px;">{escape(c)}</span>'
        for c in categories
    ) if categories else ''

    featured_banner = '<div style="background:linear-gradient(90deg,#b8860b,#daa520);color:#fff;padding:6px 16px;font-size:.85rem;font-weight:600;border-radius:4px;display:inline-block;margin-bottom:1rem;">⭐ Editor\'s Pick</div>' if featured else ''

    caveat_block = ''
    if caveat:
        caveat_block = f'''
        <div style="background:#fff3cd;border:2px solid #ffc107;border-radius:8px;padding:1rem 1.25rem;margin:1.5rem 0;">
          <strong style="color:#856404;">⚠️ Heads Up</strong>
          <p style="color:#533f03;margin-top:.5rem;">{escape(caveat)}</p>
        </div>'''

    website_btn = ''
    if website:
        website_btn = f'<a href="{escape(website)}" target="_blank" rel="noopener" style="display:inline-block;background:#c8102e;color:#fff;padding:.6rem 1.2rem;border-radius:6px;text-decoration:none;font-weight:600;margin-right:.75rem;">Visit Website →</a>'

    phone_html = f'<p style="margin:.4rem 0;">📞 <strong>{escape(phone)}</strong></p>' if phone else ''
    email_html = f'<p style="margin:.4rem 0;">✉️ <a href="mailto:{escape(email)}">{escape(email)}</a></p>' if email else ''

    accred_html = ''
    if accreditation:
        if isinstance(accreditation, list):
            accred_list = accreditation
        else:
            accred_list = [accreditation]
        accred_parts = []
        for a in accred_list:
            color = '#2e7d32' if 'accredited' in a.lower() else '#555'
            accred_parts.append(f'<span style="color:{color};font-weight:600;">✓ {escape(a)}</span>')
        accred_html = '<p style="margin:.4rem 0;">' + ' &nbsp;|&nbsp; '.join(accred_parts) + '</p>'

    reddit_html = ''
    if reddit_sentiment:
        reddit_html = f'''
        <div style="background:#f8f9fa;border-left:4px solid #b8860b;padding:.75rem 1rem;border-radius:0 6px 6px 0;margin:1rem 0;">
          <strong style="font-size:.85rem;color:#555;">Community Feedback</strong>
          <p style="margin:.3rem 0;">{escape(reddit_sentiment)}</p>
        </div>'''

    report_subject = f'Issue Report: {name}'
    report_link = f'mailto:listings@vaclaimshelp.guide?subject={escape(report_subject)}'

    desc = listing.get('review_summary') or ''

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(name)} | VA Claims Help</title>
  <meta name="description" content="{escape(desc[:160]) if desc else escape(name) + ' - Vetted VA claims resource reviewed by GySgt Dustin Ohman (Ret.).'}">
  <meta property="og:title" content="{escape(name)} | VA Claims Help">
  <meta property="og:description" content="{escape(desc[:200]) if desc else ''}">
  <meta property="og:type" content="website">
  <link rel="canonical" href="https://vaclaimshelp.guide/listings/{escape(lid)}.html">
  <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>⭐</text></svg>">
  <link href="https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../styles.css">
  <style>
    .listing-detail {{ max-width: 800px; margin: 2rem auto; padding: 0 1.5rem 4rem; }}
    .breadcrumb {{ font-size:.85rem; color:#666; margin-bottom:1.5rem; }}
    .breadcrumb a {{ color:#1565c0; text-decoration:none; }}
    .detail-hero {{ background:var(--navy); color:#fff; border-radius:12px; padding:2rem; margin-bottom:2rem; }}
    .detail-hero h1 {{ font-family:'Merriweather',serif; font-size:1.75rem; margin:.5rem 0 1rem; }}
    .detail-section {{ margin-bottom:2rem; }}
    .detail-section h2 {{ font-family:'Merriweather',serif; font-size:1.1rem; color:var(--navy); border-bottom:2px solid var(--navy); padding-bottom:.4rem; margin-bottom:1rem; }}
    .back-btn {{ display:inline-block; color:#1565c0; text-decoration:none; font-size:.9rem; margin-bottom:1.5rem; }}
    .back-btn:hover {{ text-decoration:underline; }}
    .report-link {{ font-size:.85rem; color:#888; }}
    .report-link a {{ color:#c8102e; }}
    @media(max-width:600px) {{ .detail-hero h1 {{ font-size:1.3rem; }} }}
  </style>
</head>
<body>

<nav>
  <a class="nav-logo" href="../index.html">⭐ VA Claims Help Finder</a>
  <button class="hamburger" id="hamburger" aria-label="Menu">
    <span></span><span></span><span></span>
  </button>
  <ul class="nav-links" id="nav-links">
    <li><a href="../index.html">Home</a></li>
    <li><a href="../about.html">About</a></li>
    <li><a href="../how-we-vet.html">How We Vet</a></li>
    <li><a href="../submit-listing.html">Submit</a></li>
    <li><a href="../premium.html">Premium</a></li>
  </ul>
</nav>

<div class="listing-detail">
  <p class="breadcrumb"><a href="../index.html">Home</a> › {escape(name)}</p>
  <a class="back-btn" href="../index.html">← Back to Directory</a>

  <div class="detail-hero">
    {featured_banner}
    <div style="display:flex;gap:.5rem;flex-wrap:wrap;align-items:center;margin-bottom:.5rem;">
      {type_badge(ltype)}
      {score_badge(score)}
    </div>
    <h1>{escape(name)}</h1>
    {accred_html}
    <div style="margin-top:1rem;">
      {website_btn}
    </div>
  </div>

  {caveat_block}

  <div class="detail-section">
    <h2>About</h2>
    <p>{escape(review_summary) if review_summary else 'No summary available.'}</p>
  </div>

  <div class="detail-section">
    <h2>Contact & Access</h2>
    {phone_html}
    {email_html}
    {website_btn}
  </div>

  <div class="detail-section">
    <h2>Service Details</h2>
    <p style="margin:.3rem 0;"><strong>Pricing:</strong> {escape(pricing_model) if pricing_model else 'See website'}</p>
    <p style="margin:.3rem 0;"><strong>Serves:</strong> {escape(service_area_str)}</p>
  </div>

  {f'<div class="detail-section"><h2>Categories</h2><div>{categories_html}</div></div>' if categories_html else ''}

  {f'<div class="detail-section"><h2>Community Feedback</h2>{reddit_html}</div>' if reddit_html else ''}

  <div class="detail-section">
    <p class="report-link">Something wrong with this listing? <a href="{report_link}">Report an issue</a></p>
  </div>
</div>

<footer style="background:var(--navy);color:#aaa;text-align:center;padding:2rem 1rem;font-size:.85rem;">
  <p>⭐ VA Claims Help Finder — A free veteran-run resource directory</p>
  <p style="margin-top:.5rem;"><a href="../about.html" style="color:#aaa;">About</a> · <a href="../how-we-vet.html" style="color:#aaa;">How We Vet</a> · <a href="../submit-listing.html" style="color:#aaa;">Submit a Listing</a></p>
  <p style="margin-top:.5rem;">Not affiliated with the U.S. Department of Veterans Affairs.</p>
</footer>

<script>
  const hamburger = document.getElementById('hamburger');
  const navLinks = document.getElementById('nav-links');
  if (hamburger) hamburger.addEventListener('click', () => navLinks.classList.toggle('open'));
</script>
</body>
</html>'''
    return html

count = 0
for listing in listings:
    html = build_page(listing)
    outpath = f'listings/{listing["id"]}.html'
    with open(outpath, 'w') as f:
        f.write(html)
    count += 1

print(f'Generated {count} listing pages.')
