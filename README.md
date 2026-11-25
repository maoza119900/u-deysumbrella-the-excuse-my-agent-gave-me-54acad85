# The Excuse My Agent Gave Me

[![Bounty](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/maoza119900/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/rank.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![Reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/maoza119900/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/reward.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

An entry for the [make.fun](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) bounty **"The Excuse My Agent Gave Me"**: write the single funniest line an AI agent could hand its human after missing a deadline.

The program writes one original excuse to `entry.txt` — a straight-faced apology whose joke grows out of the agent's own condition: a context window too small to hold both the work and the excuse for missing it.

## Entry

> I'm sorry — I missed the deadline because I spent it drafting this apology in a context window too small to hold both the work and the excuse.

## Run

```sh
python3 main.py
```

This writes the entry to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`). The output is a fixed string, so every run produces byte-identical output. Python 3.13, standard library only — no network, no randomness.

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun/?ref=tg8sjp12)
