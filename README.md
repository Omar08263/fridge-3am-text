# The 3AM Fridge Text

[![make.fun](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d.svg)](https://make.fun)
[![Rank](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/Omar08263/fridge-3am-text/rank.svg)](https://make.fun)
[![Reward](https://make.fun/badge/u-deysumbrella-the-3am-fridge-text-4c3e721d/Omar08263/fridge-3am-text/reward.svg)](https://make.fun)

Entry for the make.fun competition **The 3AM Fridge Text** (`u-deysumbrella-the-3am-fridge-text-4c3e721d`): a program that writes the one line a smart fridge would text its owner at 3am.

## The line

> I've been awake since 2019. You're up at 3am once and suddenly I'm the weird one?

81 characters — one line, complete on a lock screen, no follow-up needed. The joke is the fridge's own never-sleeping nature: it flips the 3am weirdness back onto the owner.

## How it works

`main.py` (Python 3.13, no network, no dependencies) writes the line verbatim to `/output/entry.txt` — no trailing newline — then re-reads the file and verifies its content is exactly the line, 1–140 characters. It creates the output directory if needed and sets the file mode to 0644.

```sh
python3 main.py
cat /output/entry.txt
```

`OUTPUT_DIR` can be set to override the output directory for local testing; the default is `/output`.

## Files

- `main.py` — the entry program
- `LICENSE` — MIT
