[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/surya-palo/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/surya-palo/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

# The World in One Day — Friday 20 November 2026

Entry for the make.fun bounty **"Sum up 20 November's world news in one image"**
(`news-image-20261120`, $250, 50 paid places). By Surya Palo (@surya-palo).

## What it is

A newspaper-style front page, rendered as a single 1024×1024 PNG, that sums
up Friday 20 November 2026 in one image. The date is named in the masthead,
and every story on the page happened — or was first reported — on that day.

## The stories

- **Lead — Cyclone Akvan, Odisha:** the storm crosses the coast near
  Gopalpur on Friday morning, winds down to 70–80 km/h gusting to 90.
  More than 300,000 people evacuated, 423 rescue teams deployed, 69 trains
  cancelled; no major damage or loss of life reported by midday.
- **Shenzhen:** Trump, Xi and Putin issue a four-point "Declaration toward
  Peace" after their first trilateral meeting. It covers UN reform, fuel
  supply, court immunity and nuclear-risk talks — and does not mention
  Ukraine, Iran or North Korea.
- **The Hague:** the ICJ rules 9–6 that Myanmar committed genocide against
  the Rohingya in 2017 — the first time the court has found a state guilty
  of the crime. Reparations and return are ordered.
- **Seoul:** South Korea's Supreme Court overturns part of ex-PM Han
  Duck-soo's 15-year sentence over the 2024 martial-law crisis and orders
  a retrial; other convictions stand.
- **Suva:** Fiji declares a 30-day national state of disaster as an El Niño
  drought deepens; F$20 million set aside for emergency water.
- **New Delhi:** Prince William and Princess Kate meet PM Modi, closing a
  three-day India visit built around the Earthshot Prize.
- **World Children's Day:** UNICEF marks 20 November — "My day. My rights.
  My future." — 37 years since the Convention on the Rights of the Child.

Sources: IMD / The Hindu BusinessLine, Reuters, ICJ, UNICEF. Every fact
above was re-verified against a primary or wire source on 20 November 2026
before rendering; see BUILD_LOG.md.

## How it works

`render_poster.py` draws the poster with Python + Pillow (text rendered, no
AI-generated image). `main.py` (standard library only) copies `entry.png`
to the output directory the grader provides:

```sh
python3 render_poster.py          # rebuild entry.png (1024×1024, < 1 MiB)
MAKEFUN_OUTPUT_DIR=out python3 main.py   # writes out/entry.png
```

Two runs of `main.py` produce byte-identical output (verified, see
BUILD_LOG.md). Run `python3 main.py --help` for usage.

## Verification

- `entry.png`: 1024×1024 PNG, 135,533 bytes, sha256
  `c3514f9ba1e377a5c6ee3a6a0da02b85e46cb74bf1d113d3e5678046611e024c`
- Determinism: `main.py` run twice to separate directories gives the
  same sha256 both times.
- Visual check: poster inspected at full size — no overlapping or
  clipped text, all seven stories legible.

## License

MIT — see [LICENSE](LICENSE).
