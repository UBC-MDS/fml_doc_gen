# fml_doc_generator

doc string generator

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
