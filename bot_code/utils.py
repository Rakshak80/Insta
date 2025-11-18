from pathlib import Path
import time

BASE = Path(__file__).resolve().parents[1]


def log_event(user, message, response):
    logs = BASE / "data" / "logs"
    logs.mkdir(parents=True, exist_ok=True)

    file = logs / f"log_{int(time.time())}.txt"
    with open(file, "w") as f:
        f.write(f"user: {user}\n")
        f.write(f"message: {message}\n")
        f.write(f"response: {response}\n")