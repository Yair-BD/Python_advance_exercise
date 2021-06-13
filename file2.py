from file1 import GreetingCard


class BirthdayCard(GreetingCard):

    def __init__(self, age=0):
        super().__init__()
        self._sender_age = age

    def greeting_msg(self):
        return f"{ super().greeting_msg()} Happy birthday {self._sender_age}"


if __name__ == '__main__':
    BirthdayCard()
