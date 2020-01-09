def get_user_symbols():
    import inspect

    for index, item in enumerate(inspect.stack()):
        try:
            name = item[0].f_globals["__name__"]
            if name == "__main__":
                return item[0].f_globals
        except:  # __name__ attribute does not exist
            pass
    return {}


def install_nbextension():
    print("Installing pyforest nbextension...")

    try:
        from notebook import nbextensions
    except ImportError:
        print("Error: Jupyter Notebook is not available")
        return

    nbextensions.install_nbextension_python("pyforest")
    nbextensions.enable_nbextension_python("pyforest")
    print("Successfully installed pyforest Jupyter Notebook nbextension")


def install_labextension():
    print("Installing pyforest labextension...")

    try:
        from jupyterlab import commands
    except ImportError:
        print("Error: Jupyter Lab is not available")
        return

    from pathlib import Path

    dir = Path(__file__).parent

    should_build = commands.install_extension(str(dir))
    print("Successfully installed pyforest Jupyter Lab labextension")
    if should_build:
        print("Starting JupyterLab build")
        commands.build()
        print("Successfully built JupyterLab")
