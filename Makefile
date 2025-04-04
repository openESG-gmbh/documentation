init:
	git config include.path ../.gitconfig
	uv sync --all-extras --dev
	uv run pre-commit install

s: start
start:
	uv run mkdocs serve -c

build:
	uv run mkdocs build -d dist

update:
	uv lock --upgrade
	uv sync
	uv run pre-commit autoupdate
