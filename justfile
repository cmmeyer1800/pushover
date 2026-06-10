lint:
    uv run ruff check --fix src/

test *args:
    uv run mypy src/
    uv run pytest {{args}}
