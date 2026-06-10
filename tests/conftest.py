import os

from dotenv import load_dotenv
import pytest

from pushover import PushoverClient

def pytest_addoption(parser):
    parser.addoption(
        "--integration",
        action="store_true",
        default=False,
        help="Run integration tests with real credentials",
    )


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--integration"):
        skipper = pytest.mark.skip(reason="Only run when --integration is given")
        for item in items:
            if "integration" in item.keywords:
                item.add_marker(skipper)


def pytest_configure(config):
    load_dotenv()


@pytest.fixture
def sync_client() -> PushoverClient:
    if "PUSHOVER_TOKEN" not in os.environ or "PUSHOVER_USER" not in os.environ:
        raise RuntimeError(
            "Must specify PUSHOVER_TOKEN and PUSHOVER_USER "
            "in .env or env vars to run integrations tests"
        )

    return PushoverClient(
        os.environ["PUSHOVER_TOKEN"],
        os.environ["PUSHOVER_USER"]
    )
