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


def install_extensions():
    print(
        "Starting to install pyforest extensions for Jupyter Notebook and Jupyter Lab"
    )
    print("")
    install_nbextension()
    print("")
    install_labextension()
    print("")
    print("Finished installing the pyforest Jupyter extensions")
    print("Please reload your Jupyter notebook and/or Jupyter lab browser windows")


def install_nbextension():
    print("Trying to install pyforest nbextension...")

    try:
        from notebook import nbextensions
    except ImportError:
        print(
            "Could not install pyforest Jupyter Notebook extension because Jupyter Notebook is not available"
        )
        return

    nbextensions.install_nbextension_python("pyforest")
    nbextensions.enable_nbextension_python("pyforest")
    print("")
    print("Finished installing the pyforest Jupyter Notebook nbextension")
    print("Please reload your Jupyter notebook browser window")


def install_labextension():
    print("Trying to install pyforest labextension...")

    try:
        from jupyterlab import commands
    except ImportError:
        print(
            "Could not install pyforest Jupyter Lab extension because Jupyter Lab is not available"
        )
        return

    from pathlib import Path

    dir = Path(__file__).parent

    should_build = commands.install_extension(str(dir))
    print("Successfully installed pyforest Jupyter Lab labextension")

    if should_build:
        print("")
        print("Starting JupyterLab build")
        commands.build()
        print("Successfully built JupyterLab")

    print("")
    print("Please reload your Jupyter Lab browser window")
