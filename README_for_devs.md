
## How to install the local python version during development
`pip3 install -e .`

## How to install the extensions during development
Same procedure as normal installation via the terminal:

`python -m pyforest install_extensions`

It is also possible via Python:
```python
import pyforest
pyforest.install_nbextension()
pyforest.install_labextension()  # takes 30-60s due to jupyter lab build
```
