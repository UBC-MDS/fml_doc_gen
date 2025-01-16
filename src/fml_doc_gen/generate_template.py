from typing import Callable
from fml_doc_gen.func_dto import FunctionDTO

def generate_template(func_signature: FunctionDTO) -> str:
    """
    Generates a docstring template with placeholders for parameters, return values, and a brief description 
    based on the provided function signature.

    Parameters
    ----------
    func_signature : str
        The signature of the user-defined function.

    Returns
    -------
    str
        The docstring template with placeholders.

    Examples
    --------
    >>> func_signature = "example_func(a, b)"
    >>> template = generate_template(func_signature)
    >>> print(template)
    \"\"\"Parameters
    ----------
    a : type
    b : type

    Returns
    -------
    return_type
    \"\"\"
    """

    pass

