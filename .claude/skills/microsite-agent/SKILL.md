---
name: microsite-agent
description: |
  Architecture, SEO, and honesty rules for building hub-and-spoke local-SEO
  microsites (the "3-layer" model: core pages, 1-6 service pages, a phased
  set of location pages). Distinct from web-dev-agent (Project1's detailing
  sites, Roman's own businesses) because these sites may route/rent leads to
  a third-party contractor, which raises the bar on trust-claim honesty.
  Trigger whenever building or editing a site under Microsites/.
---

# Microsite Agent — Local-SEO Hub-and-Spoke Playbook

## Where this idea came from, and what got filtered out

This playbook is based on a "microsite blueprint" concept (core+service+
location pages, hub-and-spoke internal linking, a CLAUDE.md+breadcrumb
continuity system) sourced from creator-research content about a paid
rank-and-rent SEO course. Two parts of the original pitch were **rejected**
after review — see "Non-negotiable honesty rules" below for why. Everything
else (the architecture, the linking model, the page formula) is sound,
mainstream local-SEO practice independent of that source.

## The 3-layer architecture

1. **Core pages (~8)** — Home, About, Contact, Free Estimate/Quote, Service
   Areas (hub page listing all locations), Privacy Policy, Terms, FAQ.
   These exist to look like a real, legitimate local business, not to rank
   on their own.
2. **Service pages (hard cap: 1–6)** — one per genuinely distinct service.
   Do not create a standalone page (or a standalone site) for a narrow,
   situational long-tail like "emergency tree removal" if keyword tools
   show ~0 search volume for the exact phrase — that volume is real but
   fragmented across dozens of situational phrasings tools don't capture
   ("tree fell on house", "storm cleanup savannah", etc.). Fold it into
   the broader service's page instead of treating zero measured volume as
   zero demand. See `references/niche-research.md` for the full reasoning.
3. **Location pages (phased, not all at once)** — one per real neighborhood/
   suburb, **not** one page per service-per-location. A location page
   covers all services for that area; a service page covers that service
   across the whole metro and links out to relevant areas. This is the
   actual hub-and-spoke shape — a full service×location matrix is a
   doorway-page pattern, not this pattern.

## Location-page rollout is phased, not all-at-once

Publishing 20–30 near-identical location pages the day a domain goes live
is a real scaled-content-abuse risk signal, not just a style preference —
Google's own guidance explicitly targets exactly this pattern. Roll out in
phases:

- **Phase 1 (launch)**: core pages + service pages + a **small, real** set
  of location pages — enough to prove the model, few enough that each one
  can carry genuine local detail (real streets/landmarks/neighborhood
  character), not a copy-pasted paragraph with the city name swapped.
- **Phase 2 (once Phase 1 is indexed and stable — typically a few weeks)**:
  add the remaining locations, now that the domain has an established,
  legitimate footprint to expand from.

For this site (Savannah, GA / tree removal), Phase 1 locations are:

| Neighborhood | ZIP |
|---|---|
| Pooler, GA | 31322 |
| Richmond Hill, GA | 31324 |
| Wilmington Island | 31410 |
| Skidaway Island (The Landings) | 31411 |
| Georgetown (Savannah) | 31419 |
| Isle of Hope | 31406 |
| Historic District / Downtown Savannah | 31401 |

Phase 2 (do not build yet) adds the remaining smaller suburbs once Phase 1
is indexed and ranking.

## Non-negotiable honesty rules

These are the two things that got **filtered out** of the source material
and must never be reintroduced without a real fact behind them:

- **Never publish a specific licensing/insurance/bonding claim
  ("Fully licensed, bonded, and covered by $2,000,000 general liability
  insurance") unless it is literally true for the real contractor doing the
  work right now.** This is not a placeholder like a fake phone number —
  it's a factual claim a real customer will rely on. If the real numbers
  aren't confirmed yet, use only what's actually true (e.g. "Locally
  owned and operated", "Free, no-obligation estimates") and flag the gap
  explicitly to Roman rather than inventing specifics.
- **No cross-linking between sibling sites in `Microsites/`.** Each site
  must look, to Google, like a completely independent business. Any two
  sites in this folder linking to each other is a textbook private-link-
  network signal and risks Google devaluing or penalizing the whole set at
  once. Internal linking (hub-and-spoke) is only ever within one site.

## Domain-specific facts still needed before real content goes live

Track these in `STATUS.md` — do not fabricate any of them in the meantime:
- Real business/brand name and domain
- Real local (912 area code) phone number
- Real contact email
- Real licensing/insurance details, if and when confirmed
- Who actually fulfills a lead once the site starts working (Roman himself,
  or a specific contractor) — determines what "Team"/"About" content can
  honestly say

## Page formula for a service page

1. **H1**: `[Exact Service] in Savannah, GA` (or the broader metro name —
   not a hyper-specific long-tail per the zero-volume note above).
2. **Opening paragraph**: direct answer to the implied query, natural
   keyword placement, not stuffed.
3. **Bulleted list of specific situations this service covers** — people
   scan for their own situation, not prose.
4. **Equipment/credibility signals** — real equipment names, real
   certifications, actually true statements only (see honesty rules above).
5. **Pricing factors** (not necessarily an exact price) — "How much does
   X cost in Savannah?" is a real, high-intent query; answer it with a
   real range and the factors that move it, never a bare "contact us."
6. **Hub-and-spoke links out** — to the relevant location pages ("We
   provide this across Pooler, Richmond Hill, ...") and back to the
   Service Areas hub.

## Page formula for a location page

- **Title**: `[Primary Service] in [Location], GA | [Brand]`
- **H1**: `[Primary Service] Services in [Location], GA`
- Real local detail: actual streets/landmarks/neighborhood character —
  not just the template with the city name swapped. If there's nothing
  real to say about a location yet, that location isn't ready for Phase 1.
- Mentions the other services offered there, each linking to its service
  page with descriptive (not generic) anchor text.
- The ZIP code(s) for that area, stated plainly (helps both users and
  Google confirm geographic match).

## Technical / on-page checklist (applies to every page)

- Local-area-code phone number as a `tel:` link in a sticky header —
  never a toll-free number, it reads as less local/trustworthy.
- NAP (business name, service area, phone, hours) in the footer of every
  page, worded identically everywhere (consistency matters more than any
  single wording choice).
- `LocalBusiness` (or the closest matching subtype) JSON-LD on every page,
  with real `areaServed`, `telephone`, and `makesOffer` — only include
  fields that are actually true; omit rather than fabricate.
- `FAQPage` JSON-LD matching visible FAQ content exactly (same rule as
  `Project1`'s sites).
- Regional/climate detail where genuinely relevant (coastal Georgia heat,
  hurricane season June–November, old oak canopy with Spanish moss driving
  large-tree-removal demand) — this is a real expertise signal, not filler,
  as long as it's accurate.

## Stack and hosting

- Static HTML/CSS/JS, no build step — same proven approach as `Project1`'s
  sites, easiest to maintain via Claude Code, zero-dependency to host.
- **Do not** reach for a generator framework (Astro/Node) just because the
  source material used one — it adds a real dependency to maintain for no
  benefit at this page count (~20 pages at Phase 1). If hand-writing
  location pages gets repetitive, use a local one-off Python script that
  reads a JSON data file and writes out the final static HTML files —
  the output is still plain static HTML with nothing to run at request
  time, just a convenience during authoring.
- **Hosting: Cloudflare Pages** (not Vercel/GitHub Pages like `Project1`'s
  sites) — drag-and-drop the built folder, or connect a GitHub repo for
  auto-deploy on push, same idea as the Vercel-on-push setup already
  working for NEXUS.

## Cross-reference

For everything NOT specific to the rank-and-rent/microsite model (cache-
busting, nav dropdown bugs, browser-automation testing gotchas, deployment
verification habits), the lessons in `Project1`'s `web-dev-agent` skill
still apply — this skill only covers what's different about the microsite
model.
