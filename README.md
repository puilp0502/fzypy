# fzypy
A fuzzy finder in Python, based on [fzy](https://github.com/jhawthorn/fzy)

## Installation
```shell script
pip install fzypy
```
To build manually:
```shell script
git clone --recurse-submodules https://github.com/puilp0502/fzypy.git
cd fzypy
python setup.py install
```

## Usage
Fuzzy searching:
```python
from fzy import search
entries = [
    "src/choices.c",
    "src/choices.h",
    "src/match.c",
    "src/match.h",
]
search("s/c.c", entries)
# [('src/choices.c', 2.82), ('src/match.c', 1.8399999999999999)]
```
Search results are ordered in descending order, by score.

When running multiple searches against same set of candidates, use Choice object:
```python
from fzy import Choice

entries = [
    "src/choices.c",
    "src/choices.h",
    "src/match.c",
    "src/match.h",
]
choicer = Choice()
for entry in entries:
    choicer.add(entry)

choicer.search("s/c.c")
# [('src/choices.c', 2.82), ('src/match.c', 1.8399999999999999)]
choicer.search("s/m.c")
# [('src/match.c', 2.84)]
```
Calculating score:
```python
from fzy import match
match("s/c", "src/choices.c")
# 1.8400000000000007
```
