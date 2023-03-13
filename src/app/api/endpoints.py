from fastapi import APIRouter

from utils import get_quant_functions, get_function_params, evaluate_function

router = APIRouter()


@router.get("/fns")
async def get_functions() -> dict:
    """
    Get all functions from quant_package.functions.

    Returns
    -------
    results:
        JSON with all functions from quant_package.functions.
    """
    functions = get_quant_functions()
    return {"message": functions}


@router.get("/fns/{name}")
async def get_function_args(name: str):
    """
    Get all parameters of a function.

    Parameters
    ----------
    name:
        Name of the function.

    Returns
    -------
    results:
        JSON with all parameters of the function.
    """
    func_args = get_function_params(name)
    return {"message": func_args}


@router.post("/fns/{name}")
async def execute_function(name: str, data_id: int, fn_params: dict):
    """
    Executes a function with parameters.

    Parameters
    ----------
    name:
        Name of the function.
    data_id:
        ID of the data.
    fn_params:
        Parameters of the function.

    Returns
    -------
    results:
        Nested JSON with the results of the function.
    """
    params = {"data_id": data_id, **fn_params}
    results = evaluate_function(name, params)
    return {"message": results}
