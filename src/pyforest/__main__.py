def main():
    import sys

    if len(sys.argv) != 2 or sys.argv[1] != "install_extensions":
        print(USAGE)
        sys.exit(-1)

    install_nbextension()
    install_labextension()


def install_nbextension():
    try:
        from notebook import nbextensions
    except ImportError:
        # No notebook
        return

    print("Installing nbextension...")
    nbextensions.install_nbextension_python("pyforest")
    nbextensions.enable_nbextension_python("pyforest")


def install_labextension():
    try:
        from jupyterlab import commands
    except ImportError:
        # No jupyterlab
        return

    from pathlib import Path

    dir = Path(__file__).parent

    print("Installing labextension...")
    should_build = commands.install_extension(str(dir))
    if should_build:
        commands.build()


USAGE = """Usage: python -m pyforest install_extensions
	installs notebook/lab extensions
"""

if __name__ == "__main__":
    main()
