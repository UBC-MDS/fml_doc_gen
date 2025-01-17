import os
from tempfile import NamedTemporaryFile, TemporaryDirectory
import pytest
from fml_doc_gen.write_docstring_to_file import write_docstring_to_file


@pytest.fixture
def valid_docstring():
    """Fixture for a valid docstring."""
    return """
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
    """


def test_write_to_valid_file(valid_docstring):
    """Test writing the docstring to a valid file"""
    with NamedTemporaryFile(suffix=".txt",delete=False) as temp_file:
        file_path = temp_file.name  

    try:
        write_docstring_to_file(valid_docstring, output_file=file_path)

        with open(file_path, "r") as file:
            content = file.read()

        assert content.strip() == valid_docstring.strip()
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)



def test_invalid_directory(valid_docstring):
    """Test writing to a file in a non-existent directory."""
    with TemporaryDirectory() as temp_dir:
        non_existent_dir = os.path.join(temp_dir, "nonexistent")
        file_path = os.path.join(non_existent_dir, "docstring_output.txt")
        with pytest.raises(ValueError, match=f"This directory '{non_existent_dir}' does not exist"):
            write_docstring_to_file(valid_docstring, output_file=file_path)

def test_non_writable_directory(valid_docstring):
    """Test writing to a file in a non-writable directory."""
    with TemporaryDirectory() as temp_dir:
        # Make the temp_dir directory non writable
        os.chmod(temp_dir, 0o500)  
        file_path = os.path.join(temp_dir, "docstring_output.txt")
        try:
            with pytest.raises(ValueError, match=f"This directory '{temp_dir}' is not writable"):
                write_docstring_to_file(valid_docstring, output_file=file_path)
        finally:
            os.chmod(temp_dir, 0o700)  