> [!NOTE]
> Project continues at https://tangled.org/radovan.xyz/cicero

The original version was written in 2015. In 2026, I rewrote it and move it to
https://tangled.org/radovan.xyz/cicero

Reasons for the rewrite:
- Less code, simpler setup, cleaner API, easier to explain and hopefully easier
  to understand.
- I wanted easier and cheaper maintenance and move to a different cloud service.
- I wanted to experiment with [Tangled](https://tangled.org/).
- Version-pinning of JS (and CSS) moved from the URL to the Markdown and is now
  in the hands of the user. I believe this makes slide decks more future-proof
  and gives me less headaches with backwards compatibility and reproducibility.
- I wanted to get rid of some hidden defaults and accidental defaults but was
  worried that removing them would break users' slide decks.
- More flexibility for the user: The new code now supports
  [remark](https://remarkjs.com), [reveal.js](https://revealjs.com), and
  [marp](https://marp.app).
- The command-line tool has been rewritten to Rust. Not because this is
  fashionable but because it makes me more calm going forward. The command-line
  tool is self-contained, less brittle, and more flexible. But I understand
  that `cargo install` is not the same as `pip install` for many users.

Follow-up:
- I will keep https://cicero.xyz/ alive for a bit and search through logs and
  contact those who use it for their presentations and offer them help to
  migrate to the new site.
