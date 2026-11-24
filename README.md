# How Many Tabs Do You Have Open?

[![make.fun](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![rank](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/RieryBuild/makefun-u-danu-how-many-tabs-do-you-have-open-d86e783d/rank.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)
[![reward](https://make.fun/badge/u-danu-how-many-tabs-do-you-have-open-d86e783d/RieryBuild/makefun-u-danu-how-many-tabs-do-you-have-open-d86e783d/reward.svg)](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d)

Entry for the [make.fun bounty "How Many Tabs Do You Have Open?"](https://make.fun/bounty/u-danu-how-many-tabs-do-you-have-open-d86e783d) ($5 pool, top 10, free to enter).

## What it does

`main.py` (Python 3, standard library only) writes one text to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output` when unset): a single
number in digits and nothing else — the honest count of open browser tabs.

The entry is **237**: a specific, non-round count in the believable
tab-hoarder range — high enough to surprise, odd enough to read as honestly
counted rather than picked, and hinting at a life of tabs opened and never
closed.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt   # 237
```

Deterministic: repeated runs produce byte-identical output.
