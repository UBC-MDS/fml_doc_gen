# fml_doc_generator

`fml_doc_generator` is a Python package designed to automate and streamline the process of creating docstrings for user-defined functions. It helps developers maintain consistent and well-documented code by providing a framework for generating either docstring templates with placeholders or fully detailed docstrings through integration with the OpenAI API. 

At its core, `fml_doc_generator` reads the function signature and structure, generates a docstring template, and optionally communicates with OpenAI to generate a complete docstring. The package includes helper functions to handle tasks such as reading function code, generating templates, interacting with the OpenAI API, parsing responses, and writing output to a file.

By automating documentation, `fml_doc_generator` saves developers time, enhances code readability, and encourages better documentation practices. Its user-friendly design makes it a valuable tool for both small and large-scale Python projects.


## Installation

```bash
$ pip install fml_doc_generator
```

## Usage
```
from fml import generate_docstring_template

def sample_function(x, y):
    return x + y

# Generate a docstring template for the sample function
docstring = generate_docstring_template(sample_function)
print(docstring)
```

## Authors
Farhan Bin Faisal, Michael Suriawan, Lukman Lateef

## Contributing

Interested in contributing? Check out the contributing guidelines. Please note that this project is released with a Code of Conduct. By contributing to this project, you agree to abide by its terms.

## License

`fml_doc_generator` was created by Farhan Faisal, Lukman Lateef, and Michael Suriawan. It is licensed under the terms of the MIT license.

## Credits

`fml_doc_generator` was created with [`cookiecutter`](https://cookiecutter.readthedocs.io/en/latest/) and the `py-pkgs-cookiecutter` [template](https://github.com/py-pkgs/py-pkgs-cookiecutter).
