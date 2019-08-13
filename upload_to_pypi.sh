#!/bin/bash

# make sure to remove or clean up dist/ folder
python setup.py sdist
twine upload dist/*