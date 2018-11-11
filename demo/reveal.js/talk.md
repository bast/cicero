<!-- .slide: data-background="#000000" -->
## A slide with a dark background

Try to press the down arrow key.

--

<!-- .slide: data-background="#ff8888" -->
## Another slide

Try **Esc** and **F** keys.

- A bullet point
- Another convincing argument

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

An image fetched from the web:

![Sample image](https://upload.wikimedia.org/wikipedia/commons/thumb/4/4f/The_Young_Cicero_Reading.jpg/316px-The_Young_Cicero_Reading.jpg)

---

## Images (2/2)

An image stored alongside the slides:

![Sample image](img/cicero.jpg)
