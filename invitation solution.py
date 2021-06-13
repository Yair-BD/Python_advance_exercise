def hiton():
    class UnderAge(Exception):

        def __init__(self, org):
            self._org = org

        def __str__(self):
            return f"Provided argument {self._org} is not a positive integer."

        def get_org(self):
            return self._org

    def send_invitation(name, age):
        try:
            if int(age) < 18:
                raise UnderAge(age)

        except UnderAge:
            return UnderAge

        else:
            print("You should send an invite to " + name.capitalize())

        finally:
            return "I love you"

    print(send_invitation("yair", 20))


if __name__ == '__main__':
    hiton()
