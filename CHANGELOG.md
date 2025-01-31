# CHANGELOG


## v3.1.1 (2025-01-31)

### Bug Fixes

- Changed fml to fml_doc_gen in contributing.md for consistency
  ([`65f7021`](https://github.com/UBC-MDS/fml_doc_gen/commit/65f7021ba640ff2c9e430daa176b75762a67a44e))

- Changed fml to fml_doc_gen in contributing.md for consistency
  ([`ef239a8`](https://github.com/UBC-MDS/fml_doc_gen/commit/ef239a80b4e46c4f456a77ae3ab174bbfcec3997))

- Temp fixed the error on example.ipynb
  ([`189e81b`](https://github.com/UBC-MDS/fml_doc_gen/commit/189e81bb4f792b1131f14921fb6c0000207485c0))


## v3.1.0 (2025-01-31)

### Bug Fixes

- Minor fix in test_fml_doc_gen integration test
  ([`cda0fce`](https://github.com/UBC-MDS/fml_doc_gen/commit/cda0fceec667a15b4a6959469fcacfa8593a7101))

- Small bug fix in read_use_function test suite
  ([`53c0eeb`](https://github.com/UBC-MDS/fml_doc_gen/commit/53c0eebfe5db1cf7f5a1e1e40f9d62d178eba17e))

### Documentation

- Updated Jupyter notebook with auto_generate usage documentation
  ([`7a7fafe`](https://github.com/UBC-MDS/fml_doc_gen/commit/7a7fafe494b76e0011a3483f007d11478e6d7deb))

- Updated example notebook to demonstrate the usage of auto_generate - Added step-by-step
  instructions for setting up OpenAI API key - Included example function calls and expected outputs
  - Added dotenv and openai dependencies to toml

- Updated Jupyter notebook with auto_generate usage documentation
  ([`fb15a91`](https://github.com/UBC-MDS/fml_doc_gen/commit/fb15a915929fc13df0661c8007f1a95fa95a86a2))

- Updated example Jupyter notebook to demonstrate the usage of generate_docstring_template wih
  auto_generate - Added step-by-step instructions for setting up OpenAI API key - Included example
  function calls and expected outputs - Added dotenv and open ai dependency to toml file

- **readme**: Add test running instructions
  ([`9331a29`](https://github.com/UBC-MDS/fml_doc_gen/commit/9331a29e72c580b85cd670a685da90a369501aaf))

Added a section to the README detailing how to run tests using pytest and measure code coverage with
  poetry.

- **readme**: Function return type in README
  ([`8b195f0`](https://github.com/UBC-MDS/fml_doc_gen/commit/8b195f0477c885deb6b34b953553c372c8a2fd42))

### Features

- Add AI-powered docstring generation function
  ([`8df0b50`](https://github.com/UBC-MDS/fml_doc_gen/commit/8df0b50d426b534ed241485658caf6976f7bbff1))

Added `fill_docstring_with_ai` function to automatically generate detailed docstrings using OpenAI's
  GPT-4. This function takes a docstring template and function source as inputs and returns a
  completed docstring.

- Loads API key using `dotenv` - Uses OpenAI's API for docstring completion - Implements error
  handling for missing inputs and API failures

- Add PEP8 compliance and type checking to read_user_function
  ([`cf98f06`](https://github.com/UBC-MDS/fml_doc_gen/commit/cf98f061f96a7f471ebf93de32b807ce898a4245))

- Implemented explicit type checking for function input - Reformatted code to align with PEP8
  standards - Updated docstrings for clarity and consistency

Example Usage: >>> def example_func(a, b): ... return a + b ... >>> sigDTO =
  read_user_function(example_func)

- Integrate fill_docstring_with_ai (autogeneration for docstrings) with error handling
  ([`b68eb96`](https://github.com/UBC-MDS/fml_doc_gen/commit/b68eb96977a51b02c4b8b447cf95966d73bb5f89))

- Added `auto_generate` option to `generate_docstring_template` to automatically generate docstrings
  using OpenAI's API. - Implemented error handling for missing function input (`ValueError`). -
  Ensured PEP 8 compliance with proper indentation, spacing, and docstring format.

### Testing

- Add 100% coverage test suite for read_user_function
  ([`8b41bae`](https://github.com/UBC-MDS/fml_doc_gen/commit/8b41baec5e722a9757a6e2390387f90fbe92b3d2))

- Added comprehensive unit tests for `read_user_function`, covering: - Functions with and without
  parameters - Functions with type hints, default values, and return types - Functions using
  `Optional` and `None` type annotations - Complex return types such as `list[int]` - Functions
  executing return statements - Error handling for invalid input

- Future improvement: Add checks for `src` attribute inside the returned object.

- **autogen**: Achieve 100% test coverage for autogen (fill_docstring_with_ai)
  ([`f07d087`](https://github.com/UBC-MDS/fml_doc_gen/commit/f07d087d872fb87c26c2ad4ddcaddfb0adca32d2))

- Added missing test cases to cover all code paths in `fill_docstring_with_ai` - Mocked API calls to
  verify correct request formation and error handling - Ensured exceptions are raised for invalid
  inputs and API failures - Included credit for auto-generated test cases


## v3.0.4 (2025-01-30)

### Bug Fixes

- Changed GITHUB TOKEN to PAT => allows use us ruleset
  ([`3ec85d3`](https://github.com/UBC-MDS/fml_doc_gen/commit/3ec85d3b1144325b6109f41249f92236a9662412))


## v3.0.3 (2025-01-30)

### Bug Fixes

- Quick test semantic release via PR
  ([`9871081`](https://github.com/UBC-MDS/fml_doc_gen/commit/9871081492f7775ffdda9aec51d67f38fdce70b4))

- Quick typo fix for docs
  ([`c73f1d6`](https://github.com/UBC-MDS/fml_doc_gen/commit/c73f1d6d5f626d9c1f3f82928e38966e200a7811))

- Release token use
  ([`3f9e445`](https://github.com/UBC-MDS/fml_doc_gen/commit/3f9e4458428be1df92456d3fd7effc5cdd75cf7c))


## v3.0.2 (2025-01-30)

### Bug Fixes

- Quick typo fix for docs
  ([`e4280e7`](https://github.com/UBC-MDS/fml_doc_gen/commit/e4280e723d3bd424e50e069c143b6fbb5a9a43ed))


## v3.0.1 (2025-01-30)

### Bug Fixes

- Add bug feat section to readme addressed by michaels
  ([`0ed8f7a`](https://github.com/UBC-MDS/fml_doc_gen/commit/0ed8f7a2338df5633c5a9448cbedd7c49e2fe19a))

- Improve readme badges addressed by michaels
  ([`2a19a57`](https://github.com/UBC-MDS/fml_doc_gen/commit/2a19a574d355f1a3cfe6de9d2fdd5d63ae7e1f3d))


## v3.0.0 (2025-01-29)

### Bug Fixes

- Fix readme to have badge for code coverage
  ([`6d52fdd`](https://github.com/UBC-MDS/fml_doc_gen/commit/6d52fdd57778f2b33c9d4006b041d57ec9c17047))


## v2.0.0 (2025-01-29)

### Features

- Give birth to fml_doc_gen
  ([`16251cd`](https://github.com/UBC-MDS/fml_doc_gen/commit/16251cd7a22f6cfc9029bac93015260f982e53e4))

- Giving birth to fml_doc_gen
  ([`5523ea0`](https://github.com/UBC-MDS/fml_doc_gen/commit/5523ea005a0c1ee82d0e64a19c89ac4a4aab200f))


## v1.0.0 (2025-01-22)
