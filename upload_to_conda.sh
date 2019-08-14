#!/bin/bash
set -e
# Any subsequent(*) commands which fail will cause the shell script to exit immediately

OUTPUT_FOLDER="dist"
PYTHON_VERSION=(2.7 3.4 3.5 3.6 3.7)
# TODO: read username and password from separate file that is gitingored
ANACONDA_USERNAME="username"
ANACONDA_PASSWORD="password"

if [ -d ./$OUTPUT_FOLDER ]
then
    rm -rf $OUTPUT_FOLDER/*
else
	mkdir ./$OUTPUT_FOLDER
fi

platform="unknown"
bit=$(uname -m)

if [[ "$bit" == *"x86_64"* ]]; then
        bit="64"
else
        bit="32"
fi

if [[ "$OSTYPE" == *"linux"* ]]; then
        platform="linux-$bit"
elif [[ "$OSTYPE" == *"darwin"* ]]; then
        # Mac OSX
        platform="osx-$bit"
elif [[ "$OSTYPE" == "cygwin" ]]; then
        # POSIX compatibility layer and Linux environment emulation for Windows
        platform="win-$bit"
elif [[ "$OSTYPE" == "msys" ]]; then
        # Lightweight shell and GNU utilities compiled for Windows (part of MinGW)
        platform="win-$bit"
elif [[ "$OSTYPE" == *"win"* ]]; then
        # I'm not sure this can happen.
        platform="win-$bit"
else
        echo "ERROR: Unknown platform!"
        return
fi

function conda_build_for_all_python_versions () {
	echo "conda build..."
	for py in "${PYTHON_VERSION[@]}";
	do
		echo "conda build for python version $py";
		build_output_paths+=($(conda build . --python $py --output))
	done
}

function convert_conda_builds_for_all_plattforms () {
	echo "conda convert..."
	for path in "${build_output_paths[@]}";
	do
		echo "conda convert --platform all $path -o ./$OUTPUT_FOLDER/"
		conda convert --platform all $path -o ./$OUTPUT_FOLDER/
	done
}

function get_paths_to_all_packages () {
	package_paths=${build_output_paths[@]}
	for directory in ./$OUTPUT_FOLDER/*/ ; do
	    packages=$(find $directory/ -type f -exec basename {} \;)
		for package in "${packages[@]}";
		do
			package_paths+=("$directory/$package")
		done
	done
}

function anaconda_upload () {
	get_paths_to_all_packages
	echo "anaconda upload..."
	for path in "${package_paths[@]}";
	do
		echo "anaconda upload $path"
		anaconda upload $path
	done
}

#PYTHON_VERSION=()
#build_output_paths=("C:\Users\Drechsel\Anaconda3\conda-bld\win-64\pyforest-0.1.1-py35_0.tar.bz2" "C:\Users\Drechsel\Anaconda3\conda-bld\win-64\pyforest-0.1.1-py35_0.tar.bz2")
build_output_paths=()

conda_build_for_all_python_versions
convert_conda_builds_for_all_plattforms
#conda install anaconda-client
echo "anaconda login..."
anaconda login --username $ANACONDA_USERNAME --password $ANACONDA_PASSWORD
anaconda_upload
anaconda logout

echo "execution completed!"
