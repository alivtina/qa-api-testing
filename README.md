# QA API Testing Project

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

    python -m venv .venv
    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

## Running Tests

Run all tests:

    pytest -v

## Current Results

12 automated API tests passing.
