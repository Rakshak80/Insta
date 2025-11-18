class AIEngine:
    def __init__(self, config):
        self.config = config
        self.active_users = set()

    def start_ai(self, user):
        self.active_users.add(user)
        print(f"[AI] Started for {user}")

    def stop_ai(self, user):
        self.active_users.discard(user)
        print(f"[AI] Stopped for {user}")

    def edit_image(self, user):
        print(f"[AI] Editing image for {user}")