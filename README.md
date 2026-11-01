# QA API Testing Project
[![API Tests](https://github.com/alivtina/qa-api-testing/actions/workflows/tests.yml/badge.svg)](https://github.com/alivtina/qa-api-testing/actions/workflows/tests.yml)

A beginner-friendly API testing project using Python, pytest,
and the requests library.

## API Under Test

JSONPlaceholder — a free fake REST API for testing and prototyping.

## Technologies

- Python
- pytest
- requests
- REST API
- Git

## Test Coverage

The project includes:

- GET requests for existing users
- GET requests for nonexistent users
- HTTP status code validation
- JSON response validation
- POST requests for creating posts
- Parameterized tests with pytest

Note: JSONPlaceholder simulates POST requests and does not
persist newly created resources.

## Installation

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run all tests:

```bash
pytest -v
```

## Test Execution

The project contains 12 automated API tests.

Tests can be executed locally using `pytest -v`.

GitHub Actions automatically runs the test suite on every push and pull request.
