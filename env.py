class EmailTriageEnv:

    def __init__(self):
        self.emails = [
            ("Meeting with team tomorrow", "work"),
            ("Dinner tonight?", "personal"),
            ("Huge discount offer! Buy now", "promotion"),
            ("Your account security alert", "urgent"),
            ("Congratulations! You won a lottery", "spam")
        ]
        self.index = 0

    def reset(self):
        self.index = 0
        email, _ = self.emails[self.index]
        return email

    def step(self, action):

        email, label = self.emails[self.index]

        if action == label:
            reward = 1
        else:
            reward = -1

        self.index += 1

        done = self.index >= len(self.emails)

        if not done:
            next_email, _ = self.emails[self.index]
        else:
            next_email = None

        return next_email, reward, done, {}

    def state(self):
        email, _ = self.emails[self.index]
        return email