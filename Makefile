init:
	poetry install

start:
	poetry run mkdocs serve

build:
	poetry run python -m mkdocs build -d dist
