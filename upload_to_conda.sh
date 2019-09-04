#!/bin/bash
#set -e
# Any subsequent(*) commands which fail will cause the shell script to exit immediately

# ## MANUAL STEPS TO BUILD AND UPLOAD A NEW PACKAGE VERSION:
# conda build . --python <python version>
# conda build prints output path of the .tar.bz2 file
# conda convert --platform all <path of tar.bz2 file>  -o $HOME/Anaconda3/conda-bld/
# anaconda login --username <username> --password <password>
# anaconda upload <path of tar.bz2 file> (have to do that for each tar file)
# anaconda logout

PYTHON_VERSION=(3.6 3.7)

anaconda_credentials=( `cat "anaconda_credentials.txt" `)

ANACONDA_USERNAME="$(echo ${anaconda_credentials[0]}|tr -d '\n\r')"
ANACONDA_ORGANIZATION="$(echo ${anaconda_credentials[1]}|tr -d '\n\r')"
ANACONDA_PASSWORD="$(echo ${anaconda_credentials[2]}|tr -d '\n\r')"


for py_version in "${PYTHON_VERSION[@]}"
do
	conda build . --python $py_version
done

bit=$(uname -m)
if [[ "$bit" == *"x86_64"* ]]; then
        bit="64"
else
        bit="32"
fi

if [[ "$OSTYPE" == *"linux"* ]]; then
        host_platform="linux-$bit"
elif [[ "$OSTYPE" == *"darwin"* ]]; then
        # Mac OSX
        host_platform="osx-$bit"
elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
        host_platform="win-$bit"
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
        host_platform="win-$bit"
elif [[ "$OSTYPE" == *"win"* ]]; then
        # I'm not sure this can happen.
        host_platform="win-$bit"
else
        echo "ERROR: Unknown platform!"
        return
fi

cd ~
if [ -d ./Anaconda3 ]; then
	conda_build_path="Anaconda3/conda-bld"
elif [ -d ./miniconda3 ]; then
	conda_build_path="miniconda3/conda-bld"
else
	echo "ERROR: Could not determine directory of conda-build!"
    return
fi

PLATFORMS=( osx-64 linux-32 linux-64 win-32 win-64 )
find $HOME/$conda_build_path/$host_platform -name *.tar.bz2 | while read file
do
    for platform in "${PLATFORMS[@]}"
    do
       conda convert --platform $platform $file  -o $HOME/Anaconda3/conda-bld/
    done

done

anaconda login --username $ANACONDA_USERNAME --password $ANACONDA_PASSWORD

find $HOME/$conda_build_path/ -name *.tar.bz2 | while read file
do
    echo $file
    anaconda upload $file
done

anaconda logout

echo "execution completed!"
