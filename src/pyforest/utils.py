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
