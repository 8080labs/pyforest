#!/bin/bash

# make sure to remove or clean up dist/ folder
python3 setup.py sdist
twine upload dist/*