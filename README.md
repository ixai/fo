# Fraction Operations

## Installation

`fo` is published in [TestPyPI](https://test.pypi.org/project/fo/) while dependencies must be
installed from the main PyPI repository. Because of this, two separate install commands must be issued.

```sh
pip install click
pip install --index-url https://test.pypi.org/simple/ --no-deps fo
```

## Usage

```
$ fo "? 1_2/3 + 4_5/6"
```

`fo` expects a single argument with the operation to perform. The operation format is
`[?] LEFT_OPERAND OPERATOR RIGHT_OPERAND` where:
- `?` is an optional operation prefix
- `OPERATOR` is one of `+`, `-`, `*`, `/`
- `LEFT_OPERAND` and `RIGHT_OPERAND` are either:
  - integers
  - simple or improper fractions (`NOMINATOR/DENOMINATOR`)
  - mixed fractions (`WHOLE_NOMINATOR/DENOMINATOR`)

The output is the result of the operation reduced to its lowest terms, or an integer, prefixed by `=`.

```
= 6_1/2
```

## Development

**Requirements:**
- [`pipenv`](https://pipenv.readthedocs.io/)

Checkout the code and setup a clean environment using `pipenv`.

```sh
pipenv install --dev
```

`fo` is installed in the virtual environment as an editable dependency, so you can modify the code
and run `fo` without the need to rebuild the package.

The following scripts are available to verify your code.

```sh
pipenv run format
pipenv run lint
pipenv run typecheck
pipenv run test
```
