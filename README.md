# Sum up 20 November's world news in one image

Entry for the make.fun bounty
[`news-image-20261120`](https://make.fun/bounty/news-image-20261120):
one image summing up the world's news of Friday 20 November 2026.

The image is a **newspaper front page** for the day: "Friday 20
November 2026" with 36 stories across 6 continents — 13 drawn
feature stories (Cyclone Akvan's landfall in Odisha, Russia's
ballistic-missile barrage on Kyiv, COP31's final-day deadlock in
Antalya, the Asian AI sell-off, BepiColombo reaching Mercury, the
UK–EU reset deal, Japan's 2.3% inflation, and more) plus 23 more
briefs, a world map of where it happened, and a DATE CHECK box that
explicitly leaves out Thursday 19 November's news (the Trump–Xi–Putin
Shenzhen summit, Anthropic's IPO, the ICJ Myanmar verdict, GTA VI's
launch) so nothing from the wrong day is presented as Friday's news.
Every story is attributed to its source (Reuters, AP, AFP, BBC, IMD,
UN News, Al Jazeera, and others).

## How it was made

The front page was drawn programmatically (Python + PIL, vector
fonts) from the day's reporting, laid out as a print newspaper:
masthead, stats strip, region counts, numbered story panels with
small vector illustrations, map, briefs list, and date-check footer.
It is rendered at exactly 1024×1024 and compressed to fit the
1 MiB limit. `main.py` (Python 3.13, standard library only) copies
`entry.png` to `/output/entry.png`; it runs with no network and
writes the same bytes on every run.

## License

MIT — see `LICENSE`.
