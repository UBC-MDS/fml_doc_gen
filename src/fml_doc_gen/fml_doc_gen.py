from typing import Callable, Optional
from fml_doc_gen.read_user_function import read_user_function
from fml_doc_gen.generate_template import generate_template
from fml_doc_gen.write_docstring_to_file import write_docstring_to_file


def generate_docstring_template(func: Callable, output_file: Optional[str], auto_generate: Optional[bool] = False) -> str:
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
    
    f_dto = read_user_function(func)

    # TODO: Call openAI API here one day . . .
    docstring = generate_template(f_dto) if not auto_generate else "AUTO GENERATE IS NOT AVAILABLE YET!"
    
    if output_file:
        write_docstring_to_file(docstring = docstring, output_file = output_file)
    
    return docstring