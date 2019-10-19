from ._importable import LazyImport
from pathlib import Path

USER_SETTINGS_PATH = Path.home() / ".pyforest" / "user_imports.py"

TEMPLATE_TEXT = (
    "# Add your imports here, line by line\n"
    "# e.g\n"
    "# import pandas as pd\n"
    "# from pathlib import Path\n"
    "# import re"
)


def clean_line(x: str) -> str:
    return x.replace("\n", "").strip()


def is_comment(x: str) -> bool:
    return x.startswith("#")


def is_empty_line(x: str) -> bool:
    return x == ""


def is_real_import(x: str) -> bool:
    return not (is_comment(x) or is_empty_line(x))


def keep_real_imports(import_statements: list) -> list:
    return [
        import_statement
        for import_statement in import_statements
        if is_real_import(import_statement)
    ]


def clean_import_statements(import_statements: list) -> list:
    cleaned_import_statements = [
        clean_line(import_statement) for import_statement in import_statements
    ]
    return keep_real_imports(cleaned_import_statements)


def _get_import_statetments_from_user_settings(user_settings_path: str) -> list:
    file_in = open(user_settings_path, "r")
    import_statements = file_in.readlines()

    return clean_import_statements(import_statements)


def get_import_statetments_from_user_settings() -> list:
    if not USER_SETTINGS_PATH.exists():
        if not USER_SETTINGS_PATH.parent.exists():
            USER_SETTINGS_PATH.parent.mkdir()
        USER_SETTINGS_PATH.touch()
        USER_SETTINGS_PATH.write_text(TEMPLATE_TEXT)
    return _get_import_statetments_from_user_settings(USER_SETTINGS_PATH)


def assign_imports_to_global_space(import_statements: list, globals_) -> None:
    symbols = [import_statement.split()[-1] for import_statement in import_statements]

    for symbol, import_statement in zip(symbols, import_statements):
        exec(f"{symbol} = LazyImport('{import_statement}')", globals_)


def _load_user_specific_imports(globals_):
    user_import_statements = get_import_statetments_from_user_settings()
    assign_imports_to_global_space(user_import_statements, globals_)
