import pytest

from pushover import PushoverClient


@pytest.mark.integration
def test_integration_sync_client_send_message(sync_client: PushoverClient):
    resp = sync_client.send_message("test")
    assert resp.status == 1
