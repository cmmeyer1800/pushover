"""Constant definitions of pushover api parameters"""
from enum import IntEnum

V1_JSON_API = "https://api.pushover.net/1"
MESSAGES = "messages.json"


class Priority(IntEnum):
    LOWEST = -2
    LOW = -1
    NORMAL = 0
    HIGH = 1
    EMERGENCY = 2
