# VA Claims Help Finder — Site Build Instructions

Build a complete, polished, production-ready animated static website for "VA Claims Help Finder" — a veteran-run directory of vetted VA disability claims assistance companies.

## Tech Constraints
- Pure HTML + CSS + Vanilla JS ONLY — no frameworks, no npm, no build tools
- One shared CSS file: styles.css
- One shared JS file: main.js
- Google Fonts via CDN link only (Merriweather + Inter)
- All pages use relative links — site must work when deployed to Cloudflare Pages

## Color Palette
- Navy: #1a2744
- Red: #c8102e
- White: #ffffff
- Light gray: #f5f5f5
- Text: #2d2d2d

## Files to Create
1. index.html — Homepage
2. category-appeals.html — Appeals Specialists
3. category-initial-claims.html — Initial Claims Help
4. category-psych-eval.html — Psychiatric Evaluations
5. category-legal.html — Legal Representation
6. about.html — About page
7. how-we-vet.html — How We Vet Companies
8. submit-listing.html — Submit a Listing
9. premium.html — Premium Listing info
10. styles.css — All styles
11. main.js — All JS (search, animations, nav)

## Shared Nav (on every page)
Sticky header, navy background, white text:
- Left: logo "⭐ VA Claims Help Finder"
- Right: Home | Categories ▾ (dropdown: Appeals, Initial Claims, Psych Eval, Legal) | About | How We Vet | Submit | Premium
- Mobile: hamburger menu

## Shared Footer (on every page)
Navy background, white text:
- "VA Claims Help Finder — Built by a veteran, for veterans."
- contact@vaclaimshelp.guide
- Links: Home | About | How We Vet | Submit | Premium
- Disclaimer: "This directory is for informational purposes only. We do not provide legal advice."
- Copyright: © 2026 VA Claims Help Finder

## Homepage (index.html)

### Hero Section
- Full-width navy background
- Headline: "Find Trusted VA Claims Help — Vetted by a Veteran"
- Subheadline: "GySgt Dustin Ohman (Ret.) personally reviews every company listed here. No sharks. No guessing."
- CTA buttons: "Find Help Now" (red, scrolls to listings) | "How We Vet" (white outline)
- Badge: "🇺🇸 Veteran-Owned & Operated | Free to Use | Updated Weekly"

### Trust Bar
4 stats: 18M+ Veterans Served | 10 Vetted Companies | Free Directory | Updated Weekly

### Category Quick-Links (4 animated cards)
- 📋 Appeals Specialists
- 📝 Initial Claims Help
- 🧠 Psychiatric Evaluations
- ⚖️ Legal Representation

### Listings Section (id="listings")
- H2: "Vetted Companies — Updated Weekly"
- Search bar: real-time filter by name or type
- All 10 company cards in responsive grid

## Listing Card Design
- Company name (navy, bold) + Type badge (VSO=green, Claims=blue, LawFirm=purple)
- 2-sentence description
- "✓ Verified" badge if score ≥ 4
- "Visit Website →" red button (new tab)
- Fade-in animation on scroll

## Company Data

1. Veterans Guardian | vetsguardian.com | Claims Assistance | Score: 4
   "Personalized VA disability claims strategy tailored to your service record and medical history. Reports a 90% success rate in improving veteran ratings."

2. REE Medical | reemedical.com | Claims Assistance | Score: 4
   "Connects veterans with licensed medical professionals for DBQ documentation and evaluations. Helped over 95,000 veterans support their claims."

3. Wounded Warrior Project | woundedwarriorproject.org/programs/benefits-services | VSO-accredited | Score: 5
   "Nationally recognized nonprofit offering free claims assistance, C&P exam prep, and benefits navigation. No fees, ever."

4. VA Claims Insider | vaclaimsinsider.com | Claims Assistance | Score: 4
   "Coaching-based approach built by disabled veterans who know the system. No charge unless your rating improves."

5. American Legion | legion.org | VSO-accredited | Score: 5
   "Established 1919. Accredited claims representatives at local chapters nationwide — free of charge, no catch."

6. Disabled American Veterans (DAV) | dav.org | VSO-accredited | Score: 5
   "Established 1920. Free VA claims assistance and advocacy for disabled veterans. One of the most trusted names in veteran services."

7. Veteran Services Group | vsgclaims.com | Claims Assistance | Score: 3
   "Comprehensive VA claims and appeals assistance. Contingency-based fee structure — veterans pay only on successful outcomes."

8. Hill & Ponton | hillandponton.com | Law Firm | Score: 4
   "Veteran-focused disability law firm with 30+ years handling appeals and complex denied claims. Legal firepower when you need it."

9. Veterans of Foreign Wars (VFW) | vfw.org | VSO-accredited | Score: 5
   "One of the largest veteran organizations in the US. Free accredited claims help through local posts — veteran-run, veteran-trusted."

10. National Veterans Legal Services Program | nvlsp.org | Law Firm | Score: 5
    "Nonprofit legal advocacy specializing in VA benefits appeals and systemic reform. Free legal help for veterans who have been denied."

## About Page (about.html)
Tell this story in first-person from Dustin:
- 21 years USMC, retired as Gunnery Sergeant (E-7)
- Got out with 30% VA disability rating — left money on the table
- A friend told him about a private claims company; went from 30% to 80%
- That jump meant thousands more per month in benefits, for life
- The company charged ~$7,000. Worth it. But not every veteran can afford that.
- Built this directory so veterans can find legitimate help without getting ripped off
- [PHOTO PLACEHOLDER — Dustin in uniform or professional]
- CTA: "Find Help Now" → index.html#listings

## How We Vet (how-we-vet.html)
5-point quality rubric (1-5 scale):
1. Credentials & Accreditation
2. Review Score (BBB, Trustpilot, Google)
3. Pricing Transparency
4. Complaint History (FTC, BBB, VA OIG, state AG)
5. Veteran Trust Score (Reddit/Facebook community)
- Below 3.0 = not listed
- Active FTC/VA OIG complaints = immediate removal
- Updated weekly
- Fraud monitoring: VA OIG RSS, state AG, Google Alerts

## Submit a Listing (submit-listing.html)
Form: Company Name, Website, Phone, Email, Categories (checkboxes), Accreditation (select), How did you hear about us
On submit: show thank-you message, 5 business day review timeline.
Vanilla JS validation.

## Premium Page (premium.html)
3-tier comparison table:
- Basic (Free): listing only
- Premium ($49/mo): featured placement, verified badge, intake form link, priority review
- Enterprise ($99/mo): homepage featured, analytics dashboard, dedicated rep, monthly leads report
CTA: mailto:listings@vaclaimshelp.guide

## Category Pages
Each shows relevant companies from the 10 with a category hero:
- Appeals: Veterans Guardian, VA Claims Insider, Hill & Ponton, NVLSP, Veteran Services Group
- Initial Claims: Veterans Guardian, REE Medical, WWP, American Legion, DAV, VFW, VA Claims Insider
- Psych Eval: REE Medical, Veterans Guardian
- Legal: Hill & Ponton, NVLSP

## Animations (main.js + styles.css)
1. Intersection Observer: cards fade in + slide up on scroll (staggered delay)
2. Search: real-time filter on keyup
3. Nav dropdown on hover/click
4. Mobile hamburger menu
5. Smooth scroll to #listings

## SEO
Every page: unique title, meta description, og tags, canonical URL.

When done, output a list of all files created with line counts.
