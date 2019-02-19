# sphinx-automodule-example
Example sphinx automodule example to improve sphinx-markdown-builder with Restructured Text table.

## Installation

Clone repo...

```
pip install .
```

## Steps to reproduce:

```bash
cd docs
make html
make markdown
```

The differences can be seen in the built html (docs/build/html/index.html) and the built markdown (docs/build/markdown/index.md).

I.e. the methods docstrings, argument types and return types are not listed.
