import inspect
from typing import Callable, Optional

from fml_doc_gen.func_dto import FunctionDTO

def read_user_function(func: Callable) -> FunctionDTO:
    """
    Reads the source code of the user-provided function and extracts its signature and existing docstring (if any).

    Parameters
    ----------
    func : Callable
        The user-defined function.

    Returns
    -------
    FunctionDTO
        The function signature as a FunctionDTO object.

    Raises
    ------
    TypeError
        If func is not a callable object.
    
    Examples
    --------
    >>> def example_func(a, b):
    ...     return a + b
    ...
    >>> sigDTO = read_user_function(example_func)
    """
    if not callable(func):
        raise TypeError("Expected a callable function")
    
    source_lines = inspect.getsourcelines(func)
    signature = inspect.signature(func)
    name = func.__name__
   
    return_type = None if signature.return_annotation is inspect.Signature.empty else str(signature.return_annotation)
   
    inputs = []
    for param_name, param in signature.parameters.items():
        param_type = None if param.annotation is inspect.Parameter.empty else str(param.annotation)
        inputs.append((param_name, param_type))

    return FunctionDTO(name=name, output=return_type, inputs=inputs, src=source_lines)
