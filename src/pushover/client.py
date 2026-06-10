"""Pushover synchronous client"""
import httpx

from pushover.const import MESSAGES, V1_JSON_API, Priority
from pushover.errors import RequestError
from pushover.models import Response

HTTP_JSON = dict[str, str | int | bool | None]

class PushoverClient(httpx.Client):
    """Pushover API Client"""

    def __init__(self, token: str, base_url: str = V1_JSON_API) -> None:
        super().__init__(base_url=base_url)
        self.req_args: HTTP_JSON = {
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
        optional = {
            "title": title,
            "device": device,
            "html": int(html) if html is not None else None,
            "priority": priority,
            "sound": sound,
            "timestamp": timestamp,
            "ttl": ttl,
            "url": url,
            "url_title": url_title,
        }
        json: HTTP_JSON = self.req_args | {
            "user": user,
            "message": message,
            **{key: value for key, value in optional.items() if value is not None},
        }

        req_resp = self.post(MESSAGES, json=json)
        if req_resp.status_code >= httpx.codes.BAD_REQUEST:
            raise RequestError(req_resp.text)

        return Response.model_validate_json(
            req_resp.text
        )
