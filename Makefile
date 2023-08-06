init:
	poetry install

start:
	poetry run python -m mkdocs serve

build:
	poetry run python -m mkdocs build -d dist
