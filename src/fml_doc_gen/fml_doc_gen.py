from typing import Callable, Optional
from fml_doc_gen.read_user_function import read_user_function
from fml_doc_gen.generate_template import generate_template
from fml_doc_gen.write_docstring_to_file import write_docstring_to_file
from fml_doc_gen.autogen import fill_docstring_with_ai


def generate_docstring_template(
    func: Callable, 
    output_file: Optional[str] = None, 
    auto_generate: bool = False
) -> str:
    """
    Generates a docstring template for a given user-defined function.

    Parameters
    ----------
    func : Callable
        The user-defined function for which the docstring template (or full docstring) needs to be generated.
    output_file : str, optional
        The file path to write the generated docstring. Defaults to None.
    auto_generate : bool, optional
        If True, automatically generates the full docstring using an OpenAI API call. Defaults to False.

    Returns
    -------
    str
        The generated docstring template or complete docstring.

    Raises
    ------
    ValueError
        If `func` is not provided.

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
    if func is None:
        raise ValueError("The `func` parameter cannot be None.")

    func_dto = read_user_function(func)
    template = generate_template(func_dto)

    docstring = template
    if auto_generate:
        docstring = fill_docstring_with_ai(template, func_dto.src)

    if output_file:
        write_docstring_to_file(docstring=docstring, output_file=output_file)

    return docstring