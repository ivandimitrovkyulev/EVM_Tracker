import asyncio
from typing import (
    List,
    Callable,
)


async def gather_funcs(functions: List[Callable], func_args: List[list]) -> list:
    """
    Gathers all asyncio http requests to be scheduled.

    :param functions: List of function pointers to execute
    :param func_args: List of function arguments
    :return: List of all 1inch swaps
    """
    function_list = [function(*arg) for function, arg in zip(functions, func_args)]

    func_results = await asyncio.gather(*function_list)

    return func_results
