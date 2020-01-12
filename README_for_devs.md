
## How to install the local python version during development
```bash
pip install -e .  # alternatively, use pip3
```

## How to install the extensions during development
Same procedure as normal installation via the terminal:

`python -m pyforest install_extensions`

It is also possible via Python:
```python
import pyforest
pyforest.install_nbextension()
pyforest.install_labextension()  # takes 30-60s due to jupyter lab build
```

## Syntax formatting
We use `black` for formatting the Python code
