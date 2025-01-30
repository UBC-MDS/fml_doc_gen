import pytest
from unittest.mock import patch, MagicMock
from fml_doc_gen.autogen import fill_docstring_with_ai

def test_empty_template():
    """Test that empty template raises ValueError"""
    with pytest.raises(ValueError, match="The docstring template cannot be empty"):
        fill_docstring_with_ai("", "def sample_func(): pass")

def test_empty_source():
    """Test that empty source raises ValueError"""
    with pytest.raises(ValueError, match="The function source cannot be empty"):
        fill_docstring_with_ai("template", "")

@patch('fml_doc_gen.autogen.OpenAI')
@patch('fml_doc_gen.autogen.load_dotenv')
def test_successful_api_call(mock_load_dotenv, mock_openai):
    """Test successful API call with mocked response"""
    # Setup mock response
    mock_client = MagicMock()
    mock_openai.return_value = mock_client
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Generated docstring"
    mock_client.chat.completions.create.return_value = mock_response

    template = "Test template"
    source = "def test(): pass"
    
    result = fill_docstring_with_ai(template, source)
    
    # Verify the result
    assert result == "Generated docstring"
    mock_load_dotenv.assert_called_once()
    mock_client.chat.completions.create.assert_called_once()

@patch('fml_doc_gen.autogen.OpenAI')
@patch('fml_doc_gen.autogen.load_dotenv')
def test_api_error(mock_load_dotenv, mock_openai):
    """Test handling of API error"""
    # Setup mock to raise an exception
    mock_client = MagicMock()
    mock_openai.return_value = mock_client
    mock_client.chat.completions.create.side_effect = Exception("API Error")

    template = "Test template"
    source = "def test(): pass"
    
    with pytest.raises(RuntimeError, match="An unexpected error occurred"):
        fill_docstring_with_ai(template, source)

@patch('fml_doc_gen.autogen.OpenAI')
@patch('fml_doc_gen.autogen.load_dotenv')
def test_api_call_content(mock_load_dotenv, mock_openai):
    """Test that API is called with correct content"""
    # Setup mock
    mock_client = MagicMock()
    mock_openai.return_value = mock_client
    mock_response = MagicMock()
    mock_response.choices[0].message.content = "Generated docstring"
    mock_client.chat.completions.create.return_value = mock_response

    template = "Test template"
    source = "def test(): pass"
    
    fill_docstring_with_ai(template, source)
    
    # Verify the API call content
    call_args = mock_client.chat.completions.create.call_args[1]
    assert call_args['model'] == "gpt-4"
    assert len(call_args['messages']) == 2
    assert call_args['messages'][0]['role'] == "system"
    assert call_args['messages'][1]['role'] == "user"
    assert template in call_args['messages'][1]['content']
    assert source in call_args['messages'][1]['content']
