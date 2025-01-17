from typing import Callable
from fml_doc_gen.func_dto import FunctionDTO
import inspect


def read_user_function(func: Callable) -> FunctionDTO:
    """
    Reads the source code of the user-provided function and extracts its signature and existing docstring (if any).

    Parameters
    ----------
    func : Callable
        The user-defined function.

    Returns
    -------
    str
        The function signature as a string.

    Examples
    --------
    >>> def example_func(a, b):
    ...     return a + b
    ...
    >>> read_user_function(example_func)
    'example_func(a, b)'
    """
    source_lines = inspect.getsourcelines(func)
    function_header = source_lines[0][0].strip()

    name = function_header.split('(')[0].split(' ')[1]
    return_type = None
    inputs = function_header.split('(')[1].split(')')[0].split(',')
    inputs = [
        (
            thing.split(':')[0].strip(), 
            thing.split(':')[1].strip() if ':' in thing else None
        ) for thing in inputs
    ]
   
    if '->' in function_header:
        return_type = function_header.split('->')[1].split(':')[0].strip()
   
    if len(inputs) == 1 and inputs[0] == ('', None):
        inputs = []

    return FunctionDTO(name, output = return_type, inputs = inputs)