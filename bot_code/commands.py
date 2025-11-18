import json
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]

with open(BASE / "messages.json") as f:
    MSG = json.load(f)


def get_fast_message(command):
    fast = MSG["fast"]

    if command in fast:
        return fast[command]

    key = command.split()[0]
    return fast.get(key, "OK")