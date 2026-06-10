"""Pushover synchronous client"""
import httpx

from pushover.const import MESSAGES, V1_JSON_API, Priority
from pushover.errors import RequestError
from pushover.models import Response


class PushoverClient(httpx.Client):
    """Pushover API Client"""

    def __init__(self, token: str, base_url: str = V1_JSON_API) -> None:
        super().__init__(base_url=base_url)
        self.req_args = {
            "token": token
        }

    # TODO: Add attachment support
    def send_message(
        self,
        user: str,
        message: str,
        title: str | None = None,
        device: str | None = None,
        html: bool | None = None,
        priority: Priority | None = None,
        sound: str | None = None,
        timestamp: int | None = None,
        ttl: int | None = None,
        url: str | None = None,
        url_title: str | None = None,
    ) -> Response:
        """"""
        json = self.req_args | {
            "user": user,
            "message": message,
        }
        req_resp = self.post(MESSAGES, json=json)
        if req_resp.status_code >= httpx.codes.BAD_REQUEST:
            raise RequestError(req_resp.text)

        return Response.model_validate_json(
            req_resp.text
        )
