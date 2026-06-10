lint:
    uv run ruff check --fix src/

test:
    uv run mypy .
    uv run pytest
