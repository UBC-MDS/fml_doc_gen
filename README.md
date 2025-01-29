# fml_doc_gen

[![Documentation Status](https://readthedocs.org/projects/fml-doc-gen/badge/?version=latest)](https://fml-doc-gen.readthedocs.io/en/latest/?badge=latest)

## Authors

- Farhan Bin Faisal  
- Michael Suriawan  
- Lukman Lateef

## Summary

`fml_doc_gen` is a Python package designed to simplify the process of writing docstrings for user-defined functions. It offers an automated way to generate docstring templates or fully detailed docstrings through integration with the OpenAI API. By streamlining documentation, it helps developers save time, improve code readability, and maintain consistent documentation standards across projects.

## Installation

```bash
$ pip install fml_doc_gen 
```

## Usage

`generate_docstring_template` can be used to generate docstring template for your function shown below:

```python
import fml_doc_gen
from fml_doc_gen.fml_doc_gen import generate_docstring_template

def square(base: int, pow: int) -> int:
    return base ** pow

print(generate_docstring_template(square, output_file=None))
```

## Functions Included

- **`generate_docstring_template(func: Callable, output_file: str, auto_generate: bool = False) -> str`**:
  The main end-user function that generates either a docstring template with placeholders or a fully detailed docstring if `auto_generate` is set to `True`.

- **`read_user_function(func: Callable) -> str`**: 
  Reads and extracts the signature and existing docstring (if any) of a given user-defined function.

- **`generate_template(func_signature: str) -> str`**: 
  Creates a docstring template with placeholders for parameters, return values, and a brief description based on the function signature.

- **`write_docstring_to_file(docstring: str, output_file: str) -> None`**: 
  Writes the generated docstring to a specified file.

## Python Ecosystem

`fml_doc_gen` fits into the Python ecosystem as a specialized tool for automating function documentation. While other Python packages like [`sphinx`](https://www.sphinx-doc.org/) and [`pydoc`](https://docs.python.org/3/library/pydoc.html) exist for generating documentation from docstrings, there are no widely known packages that automatically generate docstrings themselves using AI. This makes `fml_doc_gen` unique in its approach by leveraging OpenAI's capabilities to produce high-quality docstrings with minimal effort from the developer.

If you are aware of a similar tool, feel free to contribute to our documentation by suggesting it!

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`fml_doc_gen` was created by Farhan Faisal, Lukman Lateef, and Michael Suriawan. It is licensed under the terms of the MIT license.

## Credits

`fml_doc_gen` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
