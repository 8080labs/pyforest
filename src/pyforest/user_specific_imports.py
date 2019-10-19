from ._importable import LazyImport
from pathlib import Path

USER_IMPORTS_PATH = Path.home() / ".pyforest" / "user_imports.py"

TEMPLATE_TEXT = (
    "# Add your imports here, line by line\n"
    "# e.g\n"
    "# import pandas as pd\n"
    "# from pathlib import Path\n"
    "# import re\n"
)


def _clean_line(x: str) -> str:
    return x.replace("\n", "").strip()


def _is_comment(x: str) -> bool:
    return x.startswith("#")


def _is_empty_line(x: str) -> bool:
    return x == ""


def _is_real_import(x: str) -> bool:
    return not (_is_comment(x) or _is_empty_line(x))


def _keep_real_imports(import_statements: list) -> list:
    return [
        import_statement
        for import_statement in import_statements
        if _is_real_import(import_statement)
    ]


def _clean_import_statements(import_statements: list) -> list:
    cleaned_import_statements = [
        _clean_line(import_statement) for import_statement in import_statements
    ]
    return _keep_real_imports(cleaned_import_statements)


def _read_import_statetments_from_user_settings(user_settings_path: str) -> list:
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


def _get_import_statetments_from_user_settings(user_imports_path) -> list:
    _maybe_init_user_imports_file(user_imports_path)
    import_statements = _read_import_statetments_from_user_settings(user_imports_path)
    return _clean_import_statements(import_statements)


def _assign_imports_to_global_space(import_statements: list, globals_) -> None:
    symbols = [import_statement.split()[-1] for import_statement in import_statements]

    for symbol, import_statement in zip(symbols, import_statements):
        exec(f"{symbol} = LazyImport('{import_statement}')", globals_)


# add user_imports_path as argument so that we can run tests on that function
def _load_user_specific_imports(
    globals_: dict, user_imports_path=USER_IMPORTS_PATH
) -> None:
    user_import_statements = _get_import_statetments_from_user_settings(
        user_imports_path
    )
    _assign_imports_to_global_space(user_import_statements, globals_)
