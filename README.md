# Sum up 20 November's world news in one image

Entry for the make.fun bounty
[`news-image-20261120`](https://make.fun/bounty/news-image-20261120):
one image summing up the world's news of Friday 20 November 2026.

The image shows the day's most consequential stories: the historic
Trump–Xi–Putin trilateral summit in Shenzhen (foreground, with the US,
Chinese and Russian flags), Russian missile strikes on Kyiv (left),
the International Court of Justice's Myanmar genocide verdict
(right, scales of justice), and Russia's airspace violation over
Poland (border marker, right edge). The date is named in the image
itself: **November 20, 2026**.

## How it was made

The image was generated with an image model from a detailed prompt
built from the day's reporting, then resized to 1024×1024, dated and
compressed to fit the 1 MiB limit. `main.py` (Python 3.13, standard
library only) copies `entry.png` to `/output/entry.png`; it runs with
no network and writes the same bytes on every run.

## License

MIT — see `LICENSE`.
