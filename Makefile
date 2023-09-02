init:
	poetry install
	poetry run pre-commit install

start:
	poetry run python -m mkdocs serve

build:
	poetry run python -m mkdocs build -d dist -c

update:
	poetry update
