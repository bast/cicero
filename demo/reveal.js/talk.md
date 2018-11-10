<!-- .slide: data-background="#000000" -->
## A slide with a dark background

Try to press arrow down.

--

<!-- .slide: data-background="#ff8888" -->
## Another slide

Try **Esc** and **F** keys.

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

---

## Images (1/2)

Slide 2

![Sample image](https://s3.amazonaws.com/static.slid.es/logo/v2/slides-symbol-512x512.png)

---

## Images (2/2)

Slide 2

![Sample image](https://s3.amazonaws.com/static.slid.es/logo/v2/slides-symbol-512x512.png)
