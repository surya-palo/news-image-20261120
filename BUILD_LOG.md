# BUILD_LOG.md — news-image-20261120

## What was built

Newspaper-style 1024×1024 poster PNG (`entry.png`) summing up Friday
20 November 2026, rendered with Python + Pillow by `render_poster.py`
(all text rendered; no AI-generated image). `main.py` (stdlib only)
copies `entry.png` to the grader's output directory.

Layout: masthead "THE WORLD IN ONE DAY — FRIDAY 20 NOVEMBER 2026",
one lead story (Cyclone Akvan) with a hand-drawn storm graphic, six
story cards, sources footer.

## Stories and verification (re-checked 20 Nov 2026, ~17:00 WIB)

- **Lead — Cyclone Akvan (20 Nov):** landfall ~08:00 near Gopalpur,
  70–80 km/h gusting to 90; 300,000+ evacuated, 423 rescue teams,
  69 trains cancelled; no major damage / loss of life reported by
  midday. Source: IMD via The Hindu BusinessLine live coverage,
  20 Nov 2026.
- **Shenzhen peace declaration (19 Nov, headline of 20 Nov):** Trump,
  Xi, Putin issue a four-point "Declaration toward Peace" after their
  first trilateral meeting; UN reform, fuel supply, court immunity,
  nuclear-risk dialogue. Does not mention Ukraine, Iran or North
  Korea. Source: Reuters wrapup (BusinessWorld / Devdiscourse),
  White House / MFA China / Kremlin texts match.
- **ICJ Rohingya verdict (19 Nov):** 9–6, Myanmar responsible for
  genocide against the Rohingya in northern Rakhine in 2017 — first
  state found guilty of genocide by the court; reparations and return
  ordered. Source: ICJ / OHCHR / IIMM.
- **South Korea (19 Nov):** Supreme Court overturns part of ex-PM Han
  Duck-soo's 15-year sentence and orders a retrial; other convictions
  upheld, detention extended 2 months. Source: Reuters / AP via
  Korea JoongAng Daily.
- **Fiji (18 Nov, reported 19 Nov):** national state of disaster for
  30 days over El Niño drought; F$20 million for emergency water;
  below-normal rain forecast until April. Source: Reuters, fiji.gov.fj.
- **New Delhi (19 Nov):** Prince William and Princess Kate meet PM
  Modi, closing a three-day India visit around the Earthshot Prize.
  Source: multiple wires / PMO statement.
- **World Children's Day (20 Nov):** UNICEF, theme "My day. My rights.
  My future." — 37 years since the Convention on the Rights of the
  Child. Source: UNICEF.

Dropped / not used: Anthropic valuation figures (contradictory numbers
across sources); US–Venezuela military-cooperation claim (single
aggregator, not verified against a wire); Kyiv embassy-strike story
(not verified against a primary source in time).

## Tests

- `python3 render_poster.py` → entry.png 1024×1024, size and sha256
  recorded below; visually inspected — no overlaps, no clipped text
  (two fixes applied: Shenzhen card body shortened, storm caption
  shortened, card body font 15→14).
- `main.py` determinism: two runs to separate output dirs
  (`MAKEFUN_OUTPUT_DIR=/tmp/mf_run1` and `/tmp/mf_run2`), sha256
  compared — byte-identical, both
  `c3514f9ba1e377a5c6ee3a6a0da02b85e46cb74bf1d113d3e5678046611e024c`,
  matching entry.png itself (`cmp` clean).
- `main.py --help` prints usage and exits 0.

## Verification

- entry.png: 1024×1024, 135,533 bytes (< 1 MiB), sha256
  `c3514f9ba1e377a5c6ee3a6a0da02b85e46cb74bf1d113d3e5678046611e024c`
- main.py runs: run 1 and run 2 sha256 identical —
  `c3514f9ba1e377a5c6ee3a6a0da02b85e46cb74bf1d113d3e5678046611e024c`
  (both runs, and entry.png itself); `cmp` clean.
- Repo: local git only (no push, no GitHub repo created by this build;
  parent handles bundling / GitHub / submission).

## Notes

- Built locally only: no submission, no wallet use, no API key, no
  credentials touched.
- `main.py` and `README.md` were each written in full and then revised
  in a later editing pass (separate commits), per the transcript-gate
  revision requirement.
