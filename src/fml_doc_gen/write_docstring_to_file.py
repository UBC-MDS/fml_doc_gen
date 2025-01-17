import os


def write_docstring_to_file(docstring: str, output_file: str = None) -> None:
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
    if output_file:
        output_dir = os.path.dirname(output_file) or "."
        if not os.path.exists(output_dir):
            raise ValueError(f"This directory '{output_dir}' does not exist.")
        
        if not os.access(output_dir, os.W_OK):
            raise ValueError(f"This directory '{output_dir}' is not writable")
            
        try:
            with open(output_file, 'w') as file:
                file.write(docstring)
        except ValueError as e:
            print(f"An error occurred while writing to the file: {e}")