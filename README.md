# Fraction Operations

## Installation

Install `fo` using your prefered python package manager. Usually `pip install fo`.

## Usage

```
$ fo "? 1_2/3 + 4_5/6"
```

`fo` expects a single argument with the operation to perform. The operation format is `[?] LEFT_OPERAND OPERATOR RIGHT_OPERAND` where:
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

The following scripts are available to verify your code.

```sh
pipenv run format
pipenv run lint
pipenv run typecheck
pipenv run test
```