init:
	poetry install

start:
	poetry run mkdocs serve

build:
	mkdocs build -d dist
