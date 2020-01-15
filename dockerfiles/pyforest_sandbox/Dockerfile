FROM jupyter/minimal-notebook

USER root

COPY ./test.ipynb ./

# Install Python 3 packages
RUN conda install --quiet --yes \
    'Cython' \
    && \
    conda clean --all -f -y

RUN pip install pyforest==1.0.1
RUN python -m pyforest install_extensions