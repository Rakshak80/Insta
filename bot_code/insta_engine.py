class InstaEngine:
    def __init__(self, config):
        self.config = config

    # ----------- PLACEHOLDER IMPLEMENTATION -----------
    def send_random_reel(self, user):
        print(f"[INSTA] Sending random reel to {user}")

    def update_bio(self, user):
        print(f"[INSTA] Bio updated")

    def send_image(self, user, message):
        print(f"[INSTA] Sending image to {user}")

    def send_friend_photo(self, user, message):
        print(f"[INSTA] Sending friend photo")

    def post_media(self, user):
        print(f"[INSTA] Media posted")

    def follow_user(self, message):
        print(f"[INSTA] Followed user: {message}")

    def unfollow_user(self, message):
        print(f"[INSTA] Unfollowed user: {message}")