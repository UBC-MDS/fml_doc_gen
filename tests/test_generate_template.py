import pytest
from fml_doc_gen.func_dto import FunctionDTO
from fml_doc_gen.generate_template import generate_template


def test_generate_template_input_type():
    """
    Test that generate_template raises a TypeError when the input is not an instance of FunctionDTO.
    """
    with pytest.raises(TypeError, match='Expected input to be FunctionDTO, got str'):
        generate_template("foo")

def test_generate_template_empty_name():
    """
    Test that generate_template raises a ValueError when the FunctionDTO name is empty.
    """
    f = FunctionDTO()
    with pytest.raises(ValueError, match='The name of the function cannot be empty!'):
        generate_template(f)

def test_generate_template_name():
    """
    Test that generate_template generates the correct template when only the name is provided.
    """
    f = FunctionDTO(name = "square")
    expected = '\n    square: \n    ### INSERT FUNCTION DEFINITION HERE ###\n    \n    \n      \n    Examples:\n    --------\n    ### INSERT FUNCTION EXAMPLE USAGES HERE ###\n'
    actual = generate_template(f)
    assert expected == actual

def test_generate_template_name_output():
    """
    Test that generate_template generates the correct template when the name and output type are provided.
    """
    f = FunctionDTO(name = "square", output="int")
    expected = '\n    square: \n    ### INSERT FUNCTION DEFINITION HERE ###\n    \n    \n    Returns:\n    -------\n    int\n        ### INSERT ADDITIONAL FUNCTION OUTPUT INFORMATION HERE ###\n\n      \n    Examples:\n    --------\n    ### INSERT FUNCTION EXAMPLE USAGES HERE ###\n'
    actual = generate_template(f)
    assert expected == actual

def test_generate_template_name_output_params_1():
    """
    Test that generate_template generates the correct template when the name, output type, 
    and parameters without specified types are provided.
    """
    f = FunctionDTO(name = "square", output="int", inputs=[('base', None), ('pow', None)])
    expected = '\n    square: \n    ### INSERT FUNCTION DEFINITION HERE ###\n    \n    Parameters:\n    ----------\n    \n    base: ...\n    ### INSERT PARAMETER DEFINITION HERE ###\n    \n\n    pow: ...\n    ### INSERT PARAMETER DEFINITION HERE ###\n    \n\n\n    \n    Returns:\n    -------\n    int\n        ### INSERT ADDITIONAL FUNCTION OUTPUT INFORMATION HERE ###\n\n      \n    Examples:\n    --------\n    ### INSERT FUNCTION EXAMPLE USAGES HERE ###\n'
    actual = generate_template(f)
    assert expected == actual

def test_generate_template_name_output_params_2():
    """
    Test that generate_template generates the correct template when the name, output type, 
    and parameters with specified types are provided.
    """
    f = FunctionDTO(name = "square", output="int", inputs=[('base', 'int'), ('pow', 'int')])
    expected = '\n    square: \n    ### INSERT FUNCTION DEFINITION HERE ###\n    \n    Parameters:\n    ----------\n    \n    base: int\n    ### INSERT PARAMETER DEFINITION HERE ###\n    \n\n    pow: int\n    ### INSERT PARAMETER DEFINITION HERE ###\n    \n\n\n    \n    Returns:\n    -------\n    int\n        ### INSERT ADDITIONAL FUNCTION OUTPUT INFORMATION HERE ###\n\n      \n    Examples:\n    --------\n    ### INSERT FUNCTION EXAMPLE USAGES HERE ###\n'
    actual = generate_template(f)
    assert expected == actual

def test_generate_template_name_params_no_output():
    """
    Test that generate_template generates the correct template when the name
    and parameters with specified types are provided, but no output type provided.
    """
    f = FunctionDTO(name = "square", output="int", inputs=[('base', 'int'), ('pow', 'int')])
    expected = '\n    square: \n    ### INSERT FUNCTION DEFINITION HERE ###\n    \n    Parameters:\n    ----------\n    \n    base: int\n    ### INSERT PARAMETER DEFINITION HERE ###\n    \n\n    pow: int\n    ### INSERT PARAMETER DEFINITION HERE ###\n    \n\n\n    \n      \n    Examples:\n    --------\n    ### INSERT FUNCTION EXAMPLE USAGES HERE ###\n'
    actual = generate_template(f)
    assert expected == actual