from fml_doc_gen import generate_template

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

    if not docstring.strip():
        raise ValueError("Could not generate docstring, please check your function is well defined")
    else:
        print("Generated Docstring:\n")
        print(docstring)
        print("\n*** End of Docstring ***\n")


    if isinstance(docstring, str) & len(output_file) > 0:
        doc_string = open(f"./{output_file}/docstring_output.txt")
        return print(doc_string)
