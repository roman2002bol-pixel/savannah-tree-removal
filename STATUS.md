# Project Status & Breadcrumb Log

## Site identity

- **Brand name**: **Savannah Tree Removal Co** (renamed 2026-09-09 — see
  "Naming correction" below. Domain: `savannahtreeremovalco.com`).
  ~~Savannah Tree Pros~~ (2026-09-07 choice, retired) — do not reuse.
- **Niche**: Tree Removal (with Emergency/Storm and Large/Hazardous as
  service pages within it, not standalone niches — see
  `.claude/skills/microsite-agent/references/niche-research.md`)
- **Market**: Savannah, GA (Chatham County metro)
- **Domain**: placeholder `savannahtreeremovalco.com` used throughout the
  code (canonical tags, JSON-LD, footer, meta) — DNS doesn't resolve as
  of 2026-09-09 (good sign), but **do a final registrar check
  (Namecheap/GoDaddy) before actually buying it** — a non-resolving
  domain isn't proof it's unregistered. Once Roman confirms the real
  domain, swap in one pass, same process used for NEXUS's domain.
- **Phone**: placeholder `(912) 555-0100` / `+19125550100` — Roman will
  buy a real 912-area-code number, swap in one pass once he has it.
- **Contact email**: placeholder `info@savannahtreeremovalco.com` —
  Roman is creating the real one now.
- **Who fulfills leads**: Roman has a contractor/plan lined up (confirmed
  2026-09-07). Licensing/experience confirmed 2026-09-08: **the
  contractor has 10 years of experience and holds all required
  licenses** — added to the site as "Licensed" + "Over 10 years of
  experience" (homepage trust-strip, footer paragraph + badge on every
  page). Still NOT confirmed, so still not on the site: business/legal
  name, liability insurance + coverage amount, bonded Y/N, specific
  certifications (e.g. ISA Certified Arborist) — no numbers or claims
  beyond "licensed"/"10 years" until those come back.
- **Logo**: the 2026-09-08 AI-generated circular badge had "SAVANNAH TREE
  PROS" traced directly into its vector artwork (potrace output — actual
  path shapes, not editable text), so the 2026-09-09 rename made it
  factually wrong and it was deleted. Replaced same-day with a
  hand-authored SVG, then **replaced again 2026-09-09 (later) with a
  second AI-generated badge** Roman regenerated himself with the correct
  name — same circular-badge concept, real tree/roots + crane/chainsaw
  illustration, "SAVANNAH TREE REMOVAL CO" / "TREE SERVICE & EMERGENCY
  REMOVAL" arced text. This export was a proper vectorization (gradients,
  ~130 paths) rather than a flat potrace trace, and its content already
  filled almost the entire 2048×1989 canvas (no huge blank-margin issue
  this time) — but it had an opaque white full-canvas background
  rectangle, which would have shown as an ugly white square on the dark
  footer. Fixed by deleting that one rect and replacing it with a white
  disc sized to just the circular badge, then tightening the viewBox to
  the actual content bounds (`"40 19 1972 1941"`) — now `images/logo.svg`
  (same filename, so no HTML changes were needed anywhere — every page
  already pointed at this path). Wired into all 20 pages' header AND
  footer as `<img class="logo-img">` next to the kept wordmark text
  (arced badge text is decorative-only at header size, confirmed by
  rendering at ~38px — same conclusion as every circular-badge logo so
  far, now checked directly each time rather than assumed). Favicon
  stayed the simple
  "STR"-on-green-square data-URI (unrelated to this badge, by design —
  see the skill's logo-workflow section on why favicons stay separate).
- **Hosting**: Cloudflare Pages (decided — this project does not use
  Vercel/GitHub Pages like the `Project1` sites). Not connected yet.
- **Stack**: static HTML/CSS/JS, no build step. No Astro/Node. Confirmed
  working via local preview (Archivo/Work Sans fonts, forest green +
  amber palette, reused the proven nav-dropdown lockedClosed pattern from
  Project1 — verified with the same hover/click test method).

## Site architecture (Phase 1 — build this first)

### Core pages (8)
- [x] `/` (Home / Hub) — built, previewed locally, nav dropdown verified
- [x] `/about.html` — built
- [x] `/contact.html` — built (quote form wired to existing `[data-quote-form]` JS contract)
- [x] `/free-estimate.html` — built (same form contract, dedicated page)
- [x] `/service-areas/index.html` — built
- [x] `/faq.html` — built 2026-09-09 (Roman: "обов'язково має бути як
      окрема вкладка" — required, not optional). Added to primary nav
      on all 19 other pages (between About and Contact). Not a copy of
      the homepage's FAQ block — a genuine synthesis: 10 questions
      grouped General / Pricing &amp; Process / Local Rules, cross-linking
      out to the relevant service and location pages (e.g. the Historic
      District permit and Landings HOA questions link to those specific
      location pages) rather than repeating their full answers verbatim.
- [x] `/privacy-policy.html` — built
- [x] `/terms.html` — built

### Service pages (5 — within the 1–6 cap)
- [x] `/services/tree-removal.html` (flagship — the broad, high-volume
      term) — built, previewed locally
- [x] `/services/emergency-storm-tree-removal.html` — built
- [x] `/services/large-hazardous-tree-removal.html` — built
- [x] `/services/tree-trimming-pruning.html` — built
- [x] `/services/stump-grinding-removal.html` — built

### Location pages — Phase 1 (7, real ZIPs verified via web search 2026-09-07)
All 7 built 2026-09-08, each with genuinely researched local detail (see
"Recent changes" below for sources) — not a templated city-name swap.
- [x] `/service-areas/pooler-ga.html` — ZIP 31322
- [x] `/service-areas/richmond-hill-ga.html` — ZIP 31324 (Bryan County, not Chatham — stated accurately on the page)
- [x] `/service-areas/wilmington-island.html` — ZIP 31410
- [x] `/service-areas/skidaway-island-the-landings.html` — ZIP 31411
- [x] `/service-areas/georgetown-savannah.html` — ZIP 31419
- [x] `/service-areas/isle-of-hope.html` — ZIP 31406
- [x] `/service-areas/historic-district-downtown-savannah.html` — ZIP 31401

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

- *2026-09-08*: Built all remaining planned pages — Roman asked for every
  page to be genuinely tied to its specific district, not templated
  ("щоб кожна сторінка була дуже добре підв'язана під кожен район"), in
  response to a pasted video about a different (WordPress/SFTP-based)
  microsite build workflow. Kept our own static-HTML/git/STATUS.md
  approach (already equivalent to that video's "LLM wiki" idea) — no
  architecture change — but adopted its one directly-relevant lesson:
  research each location for real, citable local detail before writing
  the page, instead of swapping the city name in a template. WebSearched
  each of the 7 Phase-1 areas and found genuinely distinguishing facts:
  - **Pooler**: ~34K population 2026, up ~33% since the 2020 census —
    new-construction subdivisions next to older wooded lots.
  - **Richmond Hill**: Henry & Clara Ford's winter home 1925–1947 (town
    renamed from Ways Station in his honor, 1941) — is in **Bryan
    County**, not Chatham, stated accurately on its page.
  - **Wilmington Island**: barrier island, mature live oaks over
    midcentury homes, tidal marsh/creek frontage (incl. Whitemarsh,
    Talahi).
  - **Skidaway Island/The Landings**: real, verified HOA rule — The
    Landings Association requires Public Works evaluation (Tue/Fri) for
    any tree ≥20" circumference on developed property, plus
    architectural review. [landings.org](https://landings.org/news/2020/06/03/residential-tree-removal-policy-developed-property)
  - **Georgetown**: 1970s master-planned Southside community, ~14 mi from
    downtown, near the Little Ogeechee River.
  - **Isle of Hope**: 19th-century Savannah-elite summer retreat,
    century-old live oaks on Bluff Drive, National Register district.
  - **Historic District**: real, verified City rule — Savannah's
    Landscape & Tree Protection Ordinance protects live oaks citywide;
    removing one (even on private property) generally needs a Tree
    Removal Permit backed by a certified-arborist assessment, plus a
    replacement planting; street/square trees are city property and
    can't be removed privately at all. [savannahga.gov](https://www.savannahga.gov/763/Tree-Ordinance-Administration)

  Built via a one-off Python generator script (`gen_locations.py`, kept
  in the session scratchpad, not committed — the skill explicitly
  sanctions this for repetitive location pages) reading this per-location
  data, so structure stayed consistent while content stayed genuinely
  distinct. Verified after: zero broken internal links/asset refs across
  all 19 HTML files, and FAQ visible text matches FAQPage JSON-LD exactly
  on all 7 location pages (both checked by script, not by eye).

  Also built the `/service-areas/` hub and the 5 remaining core pages
  (about/contact/free-estimate/privacy-policy/terms). Contact and
  Free Estimate both use a real form wired to `main.js`'s existing
  `[data-quote-form]`/`[data-form-status]` contract (mailto fallback,
  no backend yet). About page repeats only the already-confirmed
  licensed/10-years-experience claim — no new trust claims invented.

- *2026-09-09*: **Naming correction — "Savannah Tree Pros" retired.**
  Roman asked whether the name was good SEO-wise and pasted his own
  research claiming it collided with live competitors. Rather than trust
  the paste, verified independently: WebFetched `savannahtreepros.com`
  and `savannahgatreepros.com` directly — both are live, active
  lead-gen tree-service sites with near-identical positioning (same
  services, same service area, even a tree-ordinance mention). **This
  was my own mistake from 2026-09-07** — I picked the name without
  checking for an existing domain/business collision first. Fixed the
  process going forward (see the new "Brand name & domain vetting"
  section in `SKILL.md`) and fixed this site:
  - WebFetched 4 candidate replacement domains — none resolved via DNS
    (suggestive of availability, not proof; flagged that a final
    registrar check is still needed before purchase).
  - WebSearched each candidate's exact name for a real-business/GBP
    collision — none had an exact match; "Savannah Tree Removal Co" has
    a *soft* collision with an existing "Savannah Tree Co"
    (savannahtreeco.com) — disclosed this tradeoff to Roman explicitly
    rather than picking silently.
  - Gave Roman a real choice (not another unilateral pick) between 4
    verified-clean options; he chose **Savannah Tree Removal Co**.
  - Executed the full rebrand via a Python script across all 19 HTML
    files: title/meta/OG tags, canonical URLs, JSON-LD `name` fields,
    header/footer wordmark, copyright line, contact email, favicon
    monogram (STP → STR). Verified after: zero remaining
    "Savannah Tree Pros"/"savannahtreepros"/"STP" mentions anywhere
    (grep), zero broken internal links/asset refs (script-checked).
  - The AI-generated logo had the old name traced into its actual vector
    artwork (not editable text) — deleted it and reverted every header
    to the plain text wordmark until a new logo gets generated with the
    correct name.
  - Also added a photo background to the homepage `.hero` (Roman's
    request, same gradient-overlay treatment already used on the 5
    service-page heroes) — reused `hero-oak-savannah.jpg`, no new image
    sourcing needed.

## Next pending step

**All 20 planned Phase-1 pages are built and correctly rebranded** to
Savannah Tree Removal Co. Zero dead internal links, zero old-brand
mentions (both script-verified, not eyeballed).

- *2026-09-09*: **New logo — hand-authored SVG this time, not AI-generated.**
  Roman asked for `/faq.html` as a required standalone nav tab (was
  marked optional before) — built it: 10 questions grouped General /
  Pricing & Process / Local Rules, cross-linking to the relevant service
  and location pages rather than duplicating their answers verbatim, and
  added to primary nav on all other 19 pages (between About and
  Contact). `check_faq_schema.py` immediately caught a real ordering
  mismatch between the new page's visible FAQ order and its JSON-LD —
  fixed.

  Then Roman asked for a fresh logo, this time **hand-coded directly as
  SVG** rather than generated as a raster image and traced — avoids
  every problem the previous AI-generated logo had (huge whitespace
  canvas, name baked into non-editable artwork, illegible-at-header-size
  arced text with no way to fix any of it without regenerating from
  scratch). Design: the same circular-badge concept as the original AI
  concept Roman liked (arced brand name on top, arced tagline on bottom,
  oak-tree-with-roots silhouette center) but built from real `<text>` +
  `<textPath>` elements — the name is genuinely editable text now, not
  traced paths. Iterated visually via a local `python -m http.server`
  (browser's local-file preview sandboxes scripts, so serving it over
  HTTP was necessary to test at multiple render sizes) — first pass had
  the full brand name + a full tagline overflowing their arcs and an
  unrecognizable chainsaw-accent icon; fixed by shortening both text
  strings, correcting the arc-path geometry to true semicircles, and
  dropping the fussy tool icon in favor of a simple two-ring (amber
  outer, forest-green inner) treatment for the second brand color.
  **Added a white disc behind the whole badge** (the AI-generated
  original never had one) — this is what actually lets the same
  `images/logo.svg` file work in both the header (white background) and
  the footer (dark background) for the first time, wired into all 20
  pages' header AND footer as `<img class="logo-img">` next to the kept
  wordmark text (arced badge text is still decorative-only at header
  size, confirmed by rendering it at ~38px before finalizing — same
  reasoning as before, now backed by an actual small-size check rather
  than just applying the rule from memory).

Also waiting on (none of these block further iteration, just
real-content swaps): (1) final registrar confirmation that
`savannahtreeremovalco.com` is actually available, then purchase, (2)
real phone/email, (3) remaining licensing/insurance specifics beyond
"licensed, 10 years experience" (business/legal name, insurance
coverage, bonded Y/N, certifications).

Good next steps once those land, or if continuing without them:
commit + push + verify live (already the established workflow), then
re-run the Whitespark on-page audit
(`references/whitespark-ranking-factors-checklist.md`) now that
internal linking is fully closed up (factor #16 was the main open gap
last audit). AI-visibility optimization (schema/llms.txt pass) is the
other thing mentioned as a next step in pasted video content and still
genuinely useful to do, independent of that source.
