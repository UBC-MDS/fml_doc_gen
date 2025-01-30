import pytest
from typing import Callable, Optional
from fml_doc_gen.func_dto import FunctionDTO
from fml_doc_gen.read_user_function import read_user_function

def test_raises_error_unused_argument():
    """Test that function raises error when argument is unused"""

    with pytest.raises(TypeError, match="Expected a callable function"):
        read_user_function(5)
        
def test_no_params_no_types_no_return():
    """
    Test with a function with no input, no defined input type, 
    and no defined return type
    """
    def sample_func():
        pass

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type is None
    assert dto.inputs == []

def test_params_no_types_no_return():
    """
    Test with a function with an input, no defined input type, 
    and no defined return type
    """
    def sample_func(a):
        pass

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type is None
    assert dto.inputs == [
        ("a", None)
    ]

def test_params_types_no_return():
    """
    Test with a function with an input, input type, 
    and no defined return type
    """
    def sample_func(a: int):
        pass

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type is None
    assert dto.inputs == [
        ("a", "<class 'int'>")
    ]

def test_no_params_no_types_return():
    """
    Test with a function with no input, no input type, and a defined return type
    """
    def sample_func() -> str:
        return "hello"

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type == "<class 'str'>"
    assert dto.inputs == []

def test_params_no_types_with_return():
    """
    Test with a function with an input, no input type, 
    and a defined return type
    """
    def sample_func(a) -> bool:
        return a > 0

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type == "<class 'bool'>"
    assert dto.inputs == [
        ("a", None)
    ]

def test_params_types_with_return():
    """
    Test with a function with an input, defined input type, 
    and a defined return type
    """
    def sample_func(a: int, b: str) -> bool:
        return a > 0

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type == "<class 'bool'>"
    assert dto.inputs == [
        ("a", "<class 'int'>"),
        ("b", "<class 'str'>")
    ]

def test_params_with_all():
    """
    Test a function with input parameters, defined input types, a defined return type, 
    and a function body that executes a return statement.
    """
    def sample_func(a: int, b: str) -> bool:
        return a > 0

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type == "<class 'bool'>"
    assert dto.inputs == [
        ("a", "<class 'int'>"),
        ("b", "<class 'str'>")
    ]

def test_complex_return_type():
    """Test with a more complex return type annotation"""
    def sample_func() -> list[int]:
        return [1, 2, 3]

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type == "list[int]"
    assert dto.inputs == []

def test_default_values():
    """Test with parameters that have default values"""
    def sample_func(a: int = 0, b: str = "default"):
        pass

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type is None
    assert dto.inputs == [
        ("a", "<class 'int'>"),
        ("b", "<class 'str'>")
    ]

def test_none_type():
    """Test with None type annotations"""
    def sample_func(a: None) -> None:
        pass

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type == "None"
    assert dto.inputs == [
        ("a", "None")
    ]

def test_optional_type():
    """Test with Optional type hints"""
    
    def sample_func(a: Optional[int]) -> Optional[str]:
        pass

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert "Optional" in str(dto.output_type)
    assert "Optional" in str(dto.inputs[0][1])