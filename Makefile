.PHONY: help install test coverage lint flake8 genproto package clean test-all format

help:
	@echo "Available commands:"
	@echo "  install     - Install the package with dev dependencies using uv"
	@echo "  test        - Run tests with pytest"
	@echo "  coverage    - Run tests with coverage"
	@echo "  lint        - Run ruff linter"
	@echo "  format      - Run ruff formatter"
	@echo "  flake8      - Run flake8 linter"
	@echo "  genproto    - Generate protobuf files"
	@echo "  package     - Build package distributions"
	@echo "  test-all    - Test against multiple Python versions"
	@echo "  clean       - Clean build artifacts"

install:
	uv pip install -e ".[dev,docs]"

test:
	uv run pytest --cov=pyetcd tests/ -x -v -rxXs

coverage:
	uv run pytest --cov=pyetcd tests/ -sv

lint:
	uv run ruff check pyetcd tests

format:
	uv run ruff format pyetcd tests

flake8:
	uv run flake8

genproto:
	uv run bash python_gen.sh

package:
	uv run python -m build --sdist --wheel --outdir dist/ .

test-all:
	@echo "Testing with Python 3.8..."
	uv run --python 3.8 pytest --cov=pyetcd tests/ -x -v -rxXs
	@echo "Testing with Python 3.9..."
	uv run --python 3.9 pytest --cov=pyetcd tests/ -x -v -rxXs
	@echo "Testing with Python 3.10..."
	uv run --python 3.10 pytest --cov=pyetcd tests/ -x -v -rxXs
	@echo "Testing with Python 3.11..."
	uv run --python 3.11 pytest --cov=pyetcd tests/ -x -v -rxXs
	@echo "Testing with Python 3.12..."
	uv run --python 3.12 pytest --cov=pyetcd tests/ -x -v -rxXs
	@echo "Testing with Python 3.13..."
	uv run --python 3.13 pytest --cov=pyetcd tests/ -x -v -rxXs

clean:
	rm -rf build dist *.egg-info .coverage .pytest_cache
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
