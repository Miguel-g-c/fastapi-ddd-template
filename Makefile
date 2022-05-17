test:
	PYTHONPATH=./src/ poetry run pytest

unit-test:
	PYTHONPATH=./src/ poetry run pytest -vv ./tests/unit

integration-test:
	PYTHONPATH=./src/ poetry run pytest -vv ./tests/integration
