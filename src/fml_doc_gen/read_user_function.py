from typing import Callable
from fml_doc_gen import FunctionDTO


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

    pass

