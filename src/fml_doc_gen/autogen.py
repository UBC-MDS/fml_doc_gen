# Credit: Some test cases were auto-generated using Cursor AI.
# Additional modifications and refinements were made for completeness and correctness.

from openai import OpenAI
from dotenv import load_dotenv
import os


def fill_docstring_with_ai(docstring_template: str, function_source: str) -> str:
    """
    Generates a detailed docstring for a given function source by filling in a provided template 
    using OpenAI's language model.

    Args:
        docstring_template (str): The docstring template with placeholders for descriptions.
        function_source (str): The source code of the function to extract context.

    Returns:
        str: The completed docstring with detailed descriptions.

    Raises:
        ValueError: If either `docstring_template` or `function_source` is empty.
        RuntimeError: If the API request fails or returns an unexpected response.
    """

    if not docstring_template:
        raise ValueError("The docstring template cannot be empty.")
    
    if not function_source:
        raise ValueError("The function source cannot be empty.")

    # Load environment variables
    load_dotenv()

    # Set OpenAI API key
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    prompt = (
        "You are an expert Python programmer. Given the following function source code and a "
        "docstring template, replace the placeholders with appropriate descriptions for parameters, "
        "return values, and examples. Follow the NumPy/Google format for writing docstrings.\n\n"
        f"Docstring Template:\n{docstring_template}\n\nFunction Source:\n{function_source}"
    )

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an expert Python developer writing docstrings."},
                {"role": "user", "content": prompt},
            ]
        )

        return response.choices[0].message.content
    
    except Exception as e:
        raise RuntimeError(f"An unexpected error occurred")