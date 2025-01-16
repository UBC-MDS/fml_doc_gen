from typing import Callable
from fml_doc_gen.func_dto import FunctionDTO

def generate_docstring_template(func: Callable, output_file: str, auto_generate: bool = False) -> str:
    """
    Generates a docstring template for a given user-defined function.

    Parameters
    ----------
    func : Callable
        The user-defined function for which the docstring template (or full docstring) needs to be generated.
    output_file : str
        Writes the generated docstring to the given file. Defaults to None.
    auto_generate : bool, optional
        If True, automatically generates the full docstring using an OpenAI API call. Defaults to False.
    

    Returns
    -------
    str
        The generated docstring template or complete docstring.

    Examples
    --------
    >>> def example_func(a, b):
    ...     return a + b
    >>> docstring = generate_docstring_template(example_func)
    >>> print(docstring)
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
