#!/bin/bash

# RUN THIS SCRIPT FROM ROOT DIR (i.e. as ./tests/test_install.sh)

conda deactivate
conda env remove --name pyforest_venv

conda create -n pyforest_venv python=3.7 -y
conda activate pyforest_venv

conda install pip -y
conda install ipykernel -y

pip install jupyterlab

pip install -e .  # breaks if this script is not run from ROOT
python -m pyforest install_extensions  # current error when script run from terminal: module pyforest not found