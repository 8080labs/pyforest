#!/bin/bash
set -e
# Any subsequent(*) commands which fail will cause the shell script to exit immediately

# manual steps to build and upload new package version:
# conda build . --python <python version>
# conda build returns output path of the .tar.bz2 file
# conda convert --platform all <path of tar.bz2 file>  -o $HOME/conda-bld/
# anaconda login
# anaconda upload <path of tar.bz2 file> (have to do that for each tar file)
# repeat upload for all plattforms and python versions
# anaconda logout

PYTHON_VERSION=(3.6 3.7)
# TODO: read username and password from separate file that is gitingored
# ANACONDA_USERNAME="username"
# ANACONDA_PASSWORD="password"


echo "Building conda package ..."

# building conda packages
for py_version in "${PYTHON_VERSION[@]}"
do
	conda build . --python $py_version
done

# convert package to other platforms
cd ~
platforms=( osx-64 linux-32 linux-64 win-32 win-64 )
find $HOME/conda-bld/linux-64/ -name *.tar.bz2 | while read file
do
    echo $file
    #conda convert --platform all $file  -o $HOME/conda-bld/
    for platform in "${platforms[@]}"
    do
       conda convert --platform $platform $file  -o $HOME/conda-bld/
    done

done

#anaconda login --username $ANACONDA_USERNAME --password $ANACONDA_PASSWORD
#anaconda login

# upload packages to conda
find $HOME/conda-bld/ -name *.tar.bz2 | while read file
do
    echo $file
    anaconda upload $file
done

#anaconda logout

echo "execution completed!"
