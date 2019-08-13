#!/bin/bash

if [ -d ./dist ]
then
    echo rm -rf dist/*
fi

python3 setup.py sdist
twine upload dist/*