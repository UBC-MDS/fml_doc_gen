import os
import pytest
from fml_doc_gen.fml_doc_gen import generate_docstring_template
from tempfile import NamedTemporaryFile


@pytest.fixture
def valid_docstring():
    """Fixture for a valid docstring."""
    return """
     square: 
    ### INSERT FUNCTION DEFINITION HERE ###
    
    Parameters:
    ----------
    
    base: int
    ### INSERT PARAMETER DEFINITION HERE ###
    

    pow: int
    ### INSERT PARAMETER DEFINITION HERE ###
    


    
    Returns:
    -------
    int
        ### INSERT ADDITIONAL FUNCTION OUTPUT INFORMATION HERE ###

      
    Examples:
    --------
    ### INSERT FUNCTION EXAMPLE USAGES HERE ###
    """

# We only need one integraion test here for happy-path testing since every other functionalities have already been tested!
def test_generate_docstring_template(valid_docstring):
    def square(base: int, pow: int) -> int:
        return base**pow
    
    with NamedTemporaryFile(suffix=".txt",delete=False) as temp_file:
        file_path = temp_file.name  

    try:
        expected = '\n    square: \n    ### INSERT FUNCTION DEFINITION HERE ###\n    \n    Parameters:\n    ----------\n    \n    base: int\n    ### INSERT PARAMETER DEFINITION HERE ###\n    \n\n    pow: int\n    ### INSERT PARAMETER DEFINITION HERE ###\n    \n\n\n    \n    Returns:\n    -------\n    int\n        ### INSERT ADDITIONAL FUNCTION OUTPUT INFORMATION HERE ###\n\n      \n    Examples:\n    --------\n    ### INSERT FUNCTION EXAMPLE USAGES HERE ###\n'
        actual = generate_docstring_template(func=square, output_file=file_path, auto_generate=False)
        assert expected == actual
        
        with open(file_path, "r") as file:
            content = file.read()
        assert content.strip() == valid_docstring.strip()
    finally:
        if os.path.exists(file_path):
            os.remove(file_path)