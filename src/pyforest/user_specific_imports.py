from ._importable import LazyImport
from pathlib import Path

USER_IMPORTS_PATH = Path.home() / ".pyforest" / "user_imports.py"

TEMPLATE_TEXT = """# Add your imports here, line by line
# e.g
# import pandas as pd
# from pathlib import Path
# import re
"""


def _clean_line(x: str) -> str:
    return x.replace("\n", "").strip()


def _is_comment(x: str) -> bool:
    return x.startswith("#")


def _is_empty_line(x: str) -> bool:
    return x == ""


def _is_import_statement(x: str) -> bool:
    return not (_is_comment(x) or _is_empty_line(x))


def _find_imports(file_lines: list) -> list:
    return [file_line for file_line in file_lines if _is_import_statement(file_line)]


def _get_imports(file_lines: list) -> list:
    cleaned_lines = [_clean_line(line) for line in file_lines]
    return _find_imports(cleaned_lines)


def _read_file_lines_from_user_settings(user_settings_path: str) -> list:
    file_in = open(user_settings_path, "r")
    return file_in.readlines()


def _maybe_init_user_imports_directory(user_imports_path: Path) -> None:
    if not user_imports_path.parent.exists():
        user_imports_path.parent.mkdir(parents=True, exist_ok=True)


def _maybe_init_user_imports_file(user_imports_path: Path) -> None:
    if not user_imports_path.exists():
        _maybe_init_user_imports_directory(user_imports_path)
        user_imports_path.touch()
        user_imports_path.write_text(TEMPLATE_TEXT)


def _get_imports_from_user_settings(user_imports_path) -> list:
    _maybe_init_user_imports_file(user_imports_path)
    file_lines = _read_file_lines_from_user_settings(user_imports_path)
    return _get_imports(file_lines)


def _assign_imports_to_globals(import_statements: list, globals_) -> None:
    symbols = [import_statement.split()[-1] for import_statement in import_statements]

    for symbol, import_statement in zip(symbols, import_statements):
        exec(f"{symbol} = LazyImport('{import_statement}')", globals_)


# user_imports_path exists as argument so that we can run tests on the function
def _load_user_specific_imports(
    globals_: dict, user_imports_path=USER_IMPORTS_PATH
) -> None:
    import_statements = _get_imports_from_user_settings(user_imports_path)
    _assign_imports_to_globals(import_statements, globals_)
