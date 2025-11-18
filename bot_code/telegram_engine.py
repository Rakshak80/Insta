class TelegramEngine:
    def __init__(self, config):
        self.config = config

    def backup_message(self, user, msg):
        print(f"[TELEGRAM BACKUP] {user}: {msg}")