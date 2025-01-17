import os
import pytest
from fml_doc_gen.write_docstring_to_file import write_docstring_to_file
from tempfile import NamedTemporaryFile, TemporaryDirectory


@pytest.fixture
def valid_docstring():
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
    """

@pytest.fixture
def empty_docstring():
    """Fixture for an empty docstring."""
    return ""

def test_print_only(valid_docstring, capsys):
    """Test that the docstring prints to the screen."""
    write_docstring_to_file(valid_docstring)
    captured = capsys.readouterr()
    assert "Generated Docstring:" in captured.out
    assert valid_docstring.strip() in captured.out

def test_write_to_valid_file(valid_docstring):
    """Test writing the docstring to a valid file."""
    with NamedTemporaryFile(delete=False) as temp_file:
        file_path = temp_file.name

    try:
        write_docstring_to_file(valid_docstring, output_file=file_path)
        with open(file_path, "r") as file:
            content = file.read()
        assert content.strip() == valid_docstring.strip()
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)

def test_empty_docstring(empty_docstring):
    """Test that an empty or whitespace-only docstring raises a ValueError."""
    with pytest.raises(ValueError, match="The docstring is empty or contains only whitespace."):
        write_docstring_to_file(empty_docstring)

def test_invalid_directory(valid_docstring):
    """Test writing to a file in a non-existent directory."""
    with TemporaryDirectory() as temp_dir:
        non_existent_dir = os.path.join(temp_dir, "nonexistent")
        file_path = os.path.join(non_existent_dir, "docstring_output.txt")
        with pytest.raises(ValueError, match=f"The directory '{non_existent_dir}' does not exist."):
            write_docstring_to_file(valid_docstring, output_file=file_path)

def test_non_writable_directory(valid_docstring):
    """Test writing to a file in a non-writable directory."""
    with TemporaryDirectory() as temp_dir:
        os.chmod(temp_dir, 0o500)
        file_path = os.path.join(temp_dir, "docstring_output.txt")
        try:
            with pytest.raises(ValueError, match=f"The directory '{temp_dir}' is not writable."):
                write_docstring_to_file(valid_docstring, output_file=file_path)
        finally:
            os.chmod(temp_dir, 0o700)