class: center, middle, inverse

# Simple example presentation

## Author [@404](https://twitter.com)

Some affiliation

---

layout: true

.header-content[This is a customized header that appears on all slides]

<div id="footer-content">
  <p>
    <img src="https://mirrors.creativecommons.org/presskit/buttons/88x31/png/by.png" style="width: 100px;"/>
    This is a customized footer with an example logo that appears on all slides
  </p>
</div>

---

# Main heading

## Subheading

### Even smaller heading

Try **F** and **P** keys.

- A bullet point
- Another convincing argument

Some links:

- [Cicero](https://cicero.xyz)
- [remark](https://remarkjs.com)

---

# Slide with two columns

.left-column[
## Left heading

- Some
- Bullet
- Points
]

.right-column[
## Right heading

- Other
- Interesting
- Bullet points
]

---

## Code blocks are no problem

Here we have some Python code:

```python
from itertools import cycle

fizz = cycle(['', '', 'Fizz'])
buzz = cycle(['', '', '', '', 'Buzz'])

for i in range(1, 101):
    print((next(fizz) + next(buzz)) or i)
```

[Source](https://github.com/olemb/nonsense/blob/master/fizzbuzz/itertools_cycle.py)
