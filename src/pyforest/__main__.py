from .utils import install_extensions


USAGE = """Usage: python -m pyforest install_extensions
	installs notebook/lab extensions
"""

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2 or sys.argv[1] != "install_extensions":
        print(USAGE)
        sys.exit(-1)

    install_extensions()
