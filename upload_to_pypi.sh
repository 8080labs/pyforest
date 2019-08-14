#!/bin/bash

if [ -d ./dist ]
then
    rm -rf dist/*
fi

python3 setup.py sdist
twine upload dist/*