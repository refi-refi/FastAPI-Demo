from inspect import getmembers, isfunction

import quant_lib.functions


def get_quant_functions() -> list[str]:
    """
    Get all functions from quant_package.functions.

    Returns
    -------
    functions: list[str]
        List of all functions from quant_package.functions.
    """
    functions = getmembers(quant_lib.functions, isfunction)
    functions = [f[0] for f in functions]
    return functions


def get_function_params(fn_name: str) -> list[str]:
    """
    Get all parameters of a function.

    Parameters
    ----------
    fn_name: str
        Name of the function.

    Returns
    -------
    params: list[str]
        List of all parameters of the function.
    """
    func = getattr(quant_lib.functions, fn_name)
    return func.__code__.co_varnames


def evaluate_function(fn_name: str, fn_params: dict) -> dict:
    """
    Executes a function with parameters.

    Parameters
    ----------
    fn_name: str
        Name of the function.
    fn_params:
        Parameters of the function.

    Returns
    -------
    results: dict
        Nested JSON with the results of the function.
    """
    func = getattr(quant_lib.functions, fn_name)
    return func(**fn_params)
