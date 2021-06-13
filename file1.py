class GreetingCard:

    def __init__(self, recipient="Dana Ev", sender="Eyal Ch"):
        self._recipient = recipient
        self._sender = sender

    def greeting_msg(self):
        return f"sender:{self._sender} recipient:{self._recipient}"



if __name__ == '__main__':
    GreetingCard
