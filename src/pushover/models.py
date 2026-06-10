from uuid import UUID

from pydantic import BaseModel, ConfigDict


class Response(BaseModel):
    """Model for representing API responses from pushover"""
    model_config = ConfigDict(extra='forbid')
    status: int # TODO: enum
    request: UUID
