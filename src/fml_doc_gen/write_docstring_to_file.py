import os

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
    
    print("Generated Docstring:\n")
    print(docstring)
    print("\n*** End of Docstring ***\n")

    output_dir = os.path.dirname(output_file) or "."
    if os.path.exists(output_dir):
        raise ValueError(f"This directory '{output_dir}' does not exist.")
    
    if not os.access(output_dir, os.W_OK):
        raise ValueError(f"This directory '{output_dir}' is not writable")
        
    try:
        with open(output_dir, 'w') as file:
            file.write(docstring)
        print(f"Docstring successfully written to {output_dir}")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

        
