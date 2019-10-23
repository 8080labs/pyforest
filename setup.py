from setuptools import setup, find_packages
from setuptools.command.sdist import sdist
from setuptools.command.build_py import build_py
from setuptools.command.egg_info import egg_info
from setuptools.command.install import install
from subprocess import check_call
import platform

from src.pyforest import auto_import
from src.pyforest._version import __version__


def wrap_command(command, setup_auto_import=False):
    class DecoratedCommand(command):
        def run(self):
            suffix = ('.cmd' if platform.system() == 'Windows' else '')
            check_call(['npm' + suffix, 'install'], cwd='src/pyforest')
            check_call(['webpack' + suffix], cwd='src/pyforest')
            command.run(self)
            if setup_auto_import:
                auto_import.setup()
    return DecoratedCommand


setup_args = {
    'name': 'pyforest',
    'version': __version__,
    'include_package_data': True,
    'package_data': {
        'pyforest': ['static/*.js', 'package.json', 'package-lock.json'],
    },
    'packages': find_packages(),
    'zip_safe': False,
    'cmdclass': {
        'install': wrap_command(install, setup_auto_import=True),
        'build_py': wrap_command(build_py),
        'egg_info': wrap_command(egg_info),
        'sdist': wrap_command(sdist),
    },
    'author': '8080labs',
    'url': 'https://github.com/8080labs/pyforest',
    'keywords': [
        'ipython',
        'jupyter',
        'jupyterlab',
    ],
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Framework :: IPython',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3',
    ],
}


if __name__ == "__main__":
    setup(**setup_args)
