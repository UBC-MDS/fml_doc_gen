import pytest
from fml_doc_gen.func_dto import FunctionDTO
from fml_doc_gen.read_user_function import read_user_function


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
    assert dto.output_type == None
    assert dto.inputs == [('a', 'int')]

def test_no_params_no_types_return():
    """
    Test with a function with no input, no input type, and a defined return type
    """
    def sample_func() -> str:
        return "hello"

    dto = read_user_function(sample_func)
    assert dto.name == "sample_func"
    assert dto.output_type == "str"
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
    assert dto.output_type == "bool"
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
    assert dto.output_type == "bool"
    assert dto.inputs == [
        ("a", "int"),
        ("b", "str")
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
    assert dto.output_type == "bool"
    assert dto.inputs == [
        ("a", "int"),
        ("b", "str")
    ]