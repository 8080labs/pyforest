from .utils import install_extensions, install_nbextension, install_labextension

VALID_COMMANDS = dict(
    install_extensions=install_extensions,
    install_nbextension=install_nbextension,
    install_labextension=install_labextension,
)

USAGE = """Usage: python -m pyforest <command>
    <command>: one of install_extensions, install_nbextension, install_labextension
installs notebook/lab extensions
"""

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2 or not sys.argv[1] in VALID_COMMANDS.keys():
        print(USAGE)
        sys.exit(-1)

    install_function = VALID_COMMANDS[sys.argv[1]]
    install_function()
