init:
	git config include.path ../.gitconfig
	poetry install --no-root
	poetry run pre-commit install

s: start
start:
	poetry run python -m mkdocs serve -c

build:
	poetry run python -m mkdocs build -d dist -c

update:
	poetry update
