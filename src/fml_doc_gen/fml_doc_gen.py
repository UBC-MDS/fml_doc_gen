from typing import Callable
from fml_doc_gen import FunctionDTO


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


def write_docstring_to_file(docstring: str, output_file: str) -> None:
    """
    Writes the generated docstring to a specified output file.

    Parameters
    ----------
    docstring : str
        The docstring to be written to the file.
    output_file : str
        The path to the output file.

    Returns
    -------
    None
        This function does not return anything.

    Examples
    --------
    >>> docstring = \"\"\"Parameters
    ----------
    a : int
    b : int

    Returns
    -------
    int
    \"\"\"
    >>> output_file = 'docstring_output.txt'
    >>> write_docstring_to_file(docstring, output_file)
    # This writes the docstring to 'docstring_output.txt'
    """

    pass
