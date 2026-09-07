# Project Status & Breadcrumb Log

## Site identity

- **Niche**: Tree Removal (with Emergency/Storm and Large/Hazardous as
  service pages within it, not standalone niches — see
  `.claude/skills/microsite-agent/references/niche-research.md`)
- **Market**: Savannah, GA (Chatham County metro)
- **Domain**: **not chosen yet** — needs to be picked and purchased before
  DNS/Cloudflare setup. Candidates to consider: `savannahtreeremoval.com`,
  `savannahtreepros.com`.
- **Phone**: **not set yet** — needs a real local (912) area code number
  (see open questions below).
- **Contact email**: not set yet.
- **Who fulfills leads**: Roman has a contractor/plan lined up (confirmed
  2026-09-07) — real licensing/insurance details still needed before
  publishing any specific claim about them (see honesty rules in the
  skill — do not fabricate numbers in the meantime).
- **Hosting**: Cloudflare Pages (decided — this project does not use
  Vercel/GitHub Pages like the `Project1` sites).
- **Stack**: static HTML/CSS/JS, no build step. No Astro/Node.

## Site architecture (Phase 1 — build this first)

### Core pages (8)
- [ ] `/` (Home / Hub)
- [ ] `/about/`
- [ ] `/contact/`
- [ ] `/free-estimate/`
- [ ] `/service-areas/` (location hub — links to all Phase 1 location pages)
- [ ] `/faq/`
- [ ] `/privacy-policy/`
- [ ] `/terms/`

### Service pages (5 — within the 1–6 cap)
- [ ] `/services/tree-removal/` (flagship — the broad, high-volume term)
- [ ] `/services/emergency-storm-tree-removal/`
- [ ] `/services/large-hazardous-tree-removal/`
- [ ] `/services/tree-trimming-pruning/`
- [ ] `/services/stump-grinding-removal/`

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
  `references/niche-research.md`, and this file. No site pages built yet —
  waiting on domain/phone/email/licensing inputs above before writing real
  page content (placeholders would need real NAP data to be useful, and
  trust-claim wording specifically must not be guessed).

## Next pending step

Get answers to the 5 open questions above from Roman, then start with the
homepage + `/services/tree-removal/` (the two pages every other page links
to/from), matching the page formulas in the skill.
