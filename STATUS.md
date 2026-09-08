# Project Status & Breadcrumb Log

## Site identity

- **Brand name**: **Savannah Tree Pros** (decided 2026-09-07 — keeps
  "Savannah"+"Tree" for direct query match, "Pros" is a real, common
  pattern for trade businesses, not a stuffed exact-match domain).
- **Niche**: Tree Removal (with Emergency/Storm and Large/Hazardous as
  service pages within it, not standalone niches — see
  `.claude/skills/microsite-agent/references/niche-research.md`)
- **Market**: Savannah, GA (Chatham County metro)
- **Domain**: placeholder `savannahtreepros.com` used throughout the code
  (canonical tags, JSON-LD, footer, meta) — Roman is sourcing/confirming
  the real one ("не проблема"), swap in one pass once confirmed, same
  process used for NEXUS's domain.
- **Phone**: placeholder `(912) 555-0100` / `+19125550100` — Roman will
  buy a real 912-area-code number, swap in one pass once he has it.
- **Contact email**: placeholder `info@savannahtreepros.com` — Roman is
  creating the real one now.
- **Who fulfills leads**: Roman has a contractor/plan lined up (confirmed
  2026-09-07). Real licensing/insurance specifics requested from him
  (business/legal name, liability insurance + coverage amount if any,
  bonded Y/N, certifications e.g. ISA Certified Arborist, years in
  business) — **do not add any specific trust-claim numbers to the site
  until those answers come back**; generic-true language only
  ("Locally owned and operated", "Free estimates") until then.
- **Hosting**: Cloudflare Pages (decided — this project does not use
  Vercel/GitHub Pages like the `Project1` sites). Not connected yet.
- **Stack**: static HTML/CSS/JS, no build step. No Astro/Node. Confirmed
  working via local preview (Archivo/Work Sans fonts, forest green +
  amber palette, reused the proven nav-dropdown lockedClosed pattern from
  Project1 — verified with the same hover/click test method).

## Site architecture (Phase 1 — build this first)

### Core pages (8)
- [x] `/` (Home / Hub) — built, previewed locally, nav dropdown verified
- [ ] `/about/`
- [ ] `/contact/`
- [ ] `/free-estimate/`
- [ ] `/service-areas/` (location hub — links to all Phase 1 location pages)
- [ ] `/faq/` (optional standalone — homepage already has a real FAQ block;
      decide later if a dedicated page adds anything beyond that)
- [ ] `/privacy-policy/`
- [ ] `/terms/`

### Service pages (5 — within the 1–6 cap)
- [x] `/services/tree-removal.html` (flagship — the broad, high-volume
      term) — built, previewed locally
- [x] `/services/emergency-storm-tree-removal.html` — built
- [x] `/services/large-hazardous-tree-removal.html` — built
- [x] `/services/tree-trimming-pruning.html` — built
- [x] `/services/stump-grinding-removal.html` — built

### Location pages — Phase 1 (7, real ZIPs verified via web search 2026-09-07)
- [ ] `/service-areas/pooler-ga/` — ZIP 31322
- [ ] `/service-areas/richmond-hill-ga/` — ZIP 31324
- [ ] `/service-areas/wilmington-island/` — ZIP 31410
- [ ] `/service-areas/skidaway-island-the-landings/` — ZIP 31411
- [ ] `/service-areas/georgetown-savannah/` — ZIP 31419
- [ ] `/service-areas/isle-of-hope/` — ZIP 31406
- [ ] `/service-areas/historic-district-downtown-savannah/` — ZIP 31401

### Location pages — Phase 2 (do NOT build yet)
Add remaining smaller Savannah-metro suburbs once Phase 1 is indexed and
stable (typically a few weeks after launch) — see the phased-rollout rule
in the skill.

## Open questions blocking real content (tracked here, not guessed)

1. Domain name — pick one, confirm availability, purchase.
2. Real local phone number (912 area code).
3. Real contact email.
4. Real licensing/insurance specifics for whoever does the work, once
   confirmed — until then, use only generically-true trust language
   ("Locally owned and operated", "Free estimates"), never invented
   numbers.
5. Brand/business name for the site.

## Recent changes (breadcrumb trail)

- *2026-09-07*: Planning session. Confirmed niche (Tree Removal, Savannah
  GA), Phase 1 location list (7 areas, real ZIPs verified), hosting
  (Cloudflare Pages), stack (static HTML, no framework). Created
  `CLAUDE.md`, `.claude/skills/microsite-agent/SKILL.md` +
  `references/niche-research.md`, and this file.
- *2026-09-07*: Roman confirmed: domain/phone/email can stay placeholders
  for now (he'll swap in real ones), he has a contractor/plan lined up
  (asked for specific licensing/insurance fields, awaiting answer), and
  delegated brand naming + logo to me. Picked "Savannah Tree Pros". Built
  `css/style.css` (forest green #1b4332 + amber #d97706, Archivo + Work
  Sans), `js/main.js` (reused Project1's proven nav-dropdown pattern +
  lead-tracking scaffold), `index.html`, and
  `services/tree-removal.html`. Verified both locally via
  `python -m http.server` — nav dropdown hover/click confirmed working
  (same JS, same verification method as Project1's NEXUS site), layout
  clean at both mobile and desktop widths. Git initialized, this
  checkpoint committed.

- *2026-09-07*: Sourced real (non-AI-generated) stock photography per
  Roman's explicit instruction ("доставиш зображення на сайт. це лого не
  стосується" — deliver real images, separate from the logo work, which
  stays AI-generated via Google AI Studio). Searched Pexels directly
  (`images.pexels.com/photos/{id}/...`), screened candidates by alt text
  and visual inspection for genuine subject match — rejected several
  off-target results (willow trees, olive branches, PNW conifer forest,
  a competitor's branded safety vest) before landing on two:
  - `images/hero-oak-savannah.jpg` — Pexels photo 11577011, a sprawling
    live oak draped in Spanish moss over a garden path (matches the
    Savannah-square look, not just generic "tree").
  - `images/tree-removal-crew-savannah.jpg` — Pexels photo 6218318, a
    harnessed arborist high in a tree cutting a limb with a chainsaw
    against blue sky (genuine tree-removal action, no visible branding).
  Both downloaded at the exact 900×675 the `.img-slot` markup expects
  (verified via PIL), no watermarks, Pexels license (free for commercial
  use, no attribution required). Placeholder labels disappear
  automatically since `.img-slot` only shows them on image-load error.

- *2026-09-08*: Pushed to GitHub (`roman2002bol-pixel/savannah-tree-removal`,
  public repo) with GitHub Pages enabled for a quick shareable preview link
  while Cloudflare Pages hosting isn't connected yet — live at
  https://roman2002bol-pixel.github.io/savannah-tree-removal/. This is a
  temporary preview host, not the final production home.
- *2026-09-08*: Built the remaining 4 service pages (same formula as
  `tree-removal.html`: situations grid, equipment/process bullets, pricing-
  factors paragraph, FAQ with matching JSON-LD, area-chip cross-links,
  shared footer): `emergency-storm-tree-removal.html`,
  `large-hazardous-tree-removal.html`, `tree-trimming-pruning.html`,
  `stump-grinding-removal.html`. All 5 service pages now built — cap
  reached. Sourced one real Pexels photo per page the same way as the
  first two (search → alt-text screen → visual check for watermarks/
  competitor branding) — rejected two otherwise-good candidates
  (bucket-truck worker, pole-saw worker) after zooming in and finding a
  legible third-party company logo on their clothing. Final picks:
  `storm-tree-removal-savannah.jpg`, `large-tree-removal-savannah.jpg`,
  `tree-trimming-savannah.jpg`, `stump-grinding-savannah.jpg`, all 900×675.

## Next pending step

All 5 planned service pages are now built. Waiting on: (1) real domain
once Roman confirms it, (2) real phone/email, (3) the specific licensing/
insurance answers requested, (4) logo via Google AI Studio once Roman
grants access. None of these block continuing the build — next up is the
`/service-areas/` hub page + the 7 Phase 1 location pages (each needs
real local detail, not a templated city-name swap — see the skill's
location-page formula), then the remaining core pages (about/contact/
free-estimate/privacy/terms). Every service page already links out to
`service-areas/*.html` files that don't exist yet (same pattern
`tree-removal.html` used from the start) — those links will 404 until
the location pages are built.
