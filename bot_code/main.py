import json
import time
from pathlib import Path

from commands import get_fast_message
from insta_engine import InstaEngine
from telegram_engine import TelegramEngine
from ai_engine import AIEngine
from utils import log_event

BASE = Path(__file__).resolve().parents[1]

# Load configuration
with open(BASE / "configs" / "config.json") as f:
    CONFIG = json.load(f)

# Load messages
with open(BASE / "messages.json") as f:
    MSG = json.load(f)

# Engines
insta = InstaEngine(CONFIG)
tg = TelegramEngine(CONFIG)
ai = AIEngine(CONFIG)


def handle_command(user, message):
    cmd = message.split()[0]

    # Admin login command
    if cmd == "/admin":
        password = message.replace("/admin", "").strip()
        if password == CONFIG["admin_password"]:
            return "Admin mode on"
        return "Wrong password"

    # Fast-response commands
    response = get_fast_message(cmd)

    if cmd == "/ai":
        ai.start_ai(user)
    elif cmd == "/ai_stop":
        ai.stop_ai(user)
    elif cmd == "/reel":
        insta.send_random_reel(user)
    elif cmd == "/bio":
        insta.update_bio(user)
    elif cmd.startswith("/img"):
        insta.send_image(user, message)
    elif cmd.startswith("/friend"):
        insta.send_friend_photo(user, message)
    elif cmd == "edit":
        ai.edit_image(user)
    elif cmd == "post":
        insta.post_media(user)
    elif cmd == "follow":
        insta.follow_user(message)
    elif cmd == "unfollow":
        insta.unfollow_user(message)
    elif cmd == "/dead":
        return "Bot shutting down"

    tg.backup_message(user, message)
    log_event(user, message, response)
    return response


if __name__ == "__main__":
    print("INSTA_TESTING_BOT Running… (Demo)")