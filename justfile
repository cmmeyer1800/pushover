lint:
    uv run ruff check src/

test:
    uv run mypy .
    uv run pytest
