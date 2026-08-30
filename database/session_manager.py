class SessionManager:

    def __init__(self):
        self.sessions = {}

    def create_user(self, user_id):

        self.sessions[user_id] = {
            "left": None,
            "center": None,
            "right": None,
            "target": None,
            "state": "waiting_left",
        }

    def exists(self, user_id):
        return user_id in self.sessions

    def get(self, user_id):
        return self.sessions.get(user_id)

    def get_state(self, user_id):

        if not self.exists(user_id):
            return None

        return self.sessions[user_id]["state"]

    def set_state(self, user_id, state):

        if self.exists(user_id):
            self.sessions[user_id]["state"] = state

    def set_image(self, user_id, image_type, path):

        if self.exists(user_id):
            self.sessions[user_id][image_type] = path

    def get_image(self, user_id, image_type):

        if not self.exists(user_id):
            return None

        return self.sessions[user_id].get(image_type)

    def clear(self, user_id):

        self.sessions.pop(user_id, None)


# ✅ Entire bot will use this ONE object
session = SessionManager()