# Attention: Importable uses __double_dunder_methods__ instead of _var
# because we want to minimize the risk of collision.
# Collision happens if the imported module/object has an attribute with the same name.
# The result of collision is that the attribute of the imported module/object is masked.
# So, we are trading the risk of masking Python __builtins__ with masking module attributes
# because it will be easier to monitor the Python __builtins__
# than to monitor all attributes of libraries that might be imported with pyforest.
# Read more about dunder methods here: https://dbader.org/blog/meaning-of-underscores-in-python
class Importable(object):
    def __init__(self):
        self.__complementary_importables__ = []
        self.__was_imported__ = False

        ### the following attributes need to be initialized by the inheriting class:
        ### TODO: how to express this in a more Pytonic way?
        # self.__importable_type__ = "Importable"
        # self.__imported_name__ = None
        # self.__import_statement__ = None

    def __on_import__(self, importable):
        self.__complementary_importables__.append(importable)

    def __maybe_import_complementary_importables__(self):
        for importable in self.__complementary_importables__:
            try:
                importable.__maybe_import__()
            except:
                pass  # silently fails if the complementary importable is not available. This is because complementary importables are considered optional. Please note that direct imports of Importables will fail explicitly.

    # Python will only import the module(s) if they are missing
    # if the module(s) were imported before, this method returns immediately
    def __maybe_import__(self):
        self.__maybe_import_complementary_importables__()
        exec(self.__import_statement__, globals())
        # Attention: if the import fails, the next line will not be reached
        self.__was_imported__ = True

    # among others, called during auto-completion of IPython/Jupyter
    def __dir__(self):
        self.__maybe_import__()
        return eval(f"dir({self.__imported_name__})")

    # called for undefined attribute and returns the attribute of the imported module
    def __getattr__(self, attribute):
        self.__maybe_import__()
        return eval(f"{self.__imported_name__}.{attribute}")

    # called for callable objects, e.g. from pathlib import Path; Path(".")
    def __call__(self, *args, **kwargs):
        self.__maybe_import__()
        return eval(self.__imported_name__)(*args, **kwargs)

    def __repr__(self, *args, **kwargs):
        # it is important that __repr__ does not trigger an import if the module is not yet imported
        # e.g. if the user calls locals(), this triggers __repr__ for each object
        # and this would result in an import if the module is not yet imported
        # and those imports might fail explicitly if the module is not available
        # and this would break locals() for the user

        if self.__was_imported__:
            # next line only adds imported_name into the local scope but does not trigger a new import
            # because the importable was already imported via another trigger
            self.__maybe_import__()
            return f"active pyforest.{self.__importable_type__} of {eval(self.__imported_name__)}"
        else:
            return f"lazy pyforest.{self.__importable_type__} for '{self.__import_statement__}'"


class LazyModule(Importable):
    def __init__(self, module_name, alias=None):
        super().__init__()

        self.__importable_type__ = "LazyModule"
        if alias:
            self.__imported_name__ = alias
            self.__import_statement__ = f"import {module_name} as {alias}"
        else:
            self.__imported_name__ = module_name
            self.__import_statement__ = f"import {module_name}"


class LazyObject(Importable):
    def __init__(self, module_name, object_name, alias=None):
        super().__init__()

        self.__importable_type__ = "LazyObject"
        if alias:
            self.__imported_name__ = alias
            self.__import_statement__ = (
                f"from {module_name} import {object_name} as {alias}"
            )
        else:
            self.__imported_name__ = object_name
            self.__import_statement__ = f"from {module_name} import {object_name}"


def _import_statements(symbol_dict, was_imported=True):
    statements = []
    for _, symbol in symbol_dict.items():
        if isinstance(symbol, Importable) and (symbol.__was_imported__ == was_imported):
            print(symbol.__import_statement__)
            statements.append(symbol.__import_statement__)
    return statements
