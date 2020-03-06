# Chapter 2 - A Crash Course in Python

## Type Annotations

Recent versions of Python allow you to type annotate your code. However, they are not actully enforced by the language.

```python
def add(a: int, b: int) -> int:
    return a + b
```

Reasons to do this:

* Important form of documentation. Much easier to read when the types are explicitly written out.
* Allows you to use static analyzers ([mypy](http://mypy-lang.org/), [pytype](https://github.com/google/pytype#pytype---))
* Having to think about types forces you to write cleaner functions and interfaces.
* Helps with IDE auto-complete features.

### Examples

```python
from typing import list

def total(xs: List[float]) -> float:
    return sum(total)
```

```python
from typing import Optional

values: List[int] = []
best_so_far: Optional[float] = None
```