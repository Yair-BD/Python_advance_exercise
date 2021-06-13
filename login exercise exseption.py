def user_name_pass_ward():

    from string import punctuation as pun
    from string import digits as dig

    class UsernameContainsIllegalCharacter(Exception):

        def __init__(self, org="", let="", let_index=0):
            self._org = org
            self._let = let
            self._let_index = let_index

        def __str__(self):
            return f"Provided username '{self._org}' because {self._let}" \
                   f" in index {self._let_index}"

        def get_org(self):
            return self._org

    class UsernameTooShort(Exception):

        def __init__(self, num):
            self._num = num

        def __str__(self):
            return f"Provided username '{self._num}' because" \
                   f" the username character's smaller than 3."

    class UsernameTooLong(Exception):

        def __init__(self, num):
            self._num = num

        def __str__(self):
            return f"Provided username '{self._num}' because" \
                   f" the username is bigger than 20."

    class PasswordMissingCharacter(Exception):

        def __init__(self, pas="", char=""):
            self._pas = pas
            self._char = char

        def __str__(self):
            return f"Provided passward '{self._pas}' because" \
                   f" the passward is missed a ."

    class PasswordMissingUppercase(PasswordMissingCharacter):

        def __int__(self, pss=""):
            super().__init__(pss)

        def __str__(self):

            return f"{super.__str__(self)} (uppercase)"

    class PasswordMissingLowercase(PasswordMissingCharacter):

        def __int__(self, pss=""):
            super().__init__(pss)

        def __str__(self):
            return f"{super().__str__()} lowercase"

    class PasswordTooShort(Exception):

        def __init__(self, password=""):
            self._pas = password

        def __str__(self):
            return f"Provided passward '{self._pas}' because" \
                   f" the passward is smaller than 8 characters."

    class PasswordTooLong(Exception):

        def __init__(self, password=""):
            self._pas = password

        def __str__(self):
            return f"Provided passward '{self._pas}' because" \
                   f" the passward is longer than 40 characters."

    def username_validity(_username):
        global char_error
        for n in _username:
            if n in pun and n != "_":
                char_error = n
                raise UsernameContainsIllegalCharacter(_username, n, _username.index(n))
            else:
                continue
        if 3 > len(_username):
            raise UsernameTooShort(_username)
        elif 20 < len(_username):
            raise UsernameTooLong(_username)

    def passward_validity(_passward=""):
        p = 0
        n = 0
        if _passward.islower():
            raise PasswordMissingUppercase(_passward)
        elif _passward.isupper():
            raise PasswordMissingLowercase(_passward)
        for v in _passward:
            if v in pun:
                p += 1
        if p == 0:
            raise PasswordMissingCharacter(_passward)
        for s in _passward:
            if s not in dig:
                n += 1
        if n == 0:
            raise PasswordMissingCharacter(_passward)
        if len(_passward) > 40:
            raise PasswordTooLong(_passward)
        if len(_passward) < 8:
            raise PasswordTooShort(_passward)

    def check_input(username="", password=""):
        global char_error
        try:
            username_validity(username)
            passward_validity(password)

        except PasswordMissingUppercase:
            return f"Passward Error: {PasswordMissingUppercase(password)}"
        except PasswordMissingLowercase:
            return f"Passward Error: {PasswordMissingLowercase(password)}"
        except UsernameContainsIllegalCharacter:
            return f"Username Error: {UsernameContainsIllegalCharacter(username , char_error, username.index(char_error) + 1)}"
        except UsernameTooShort:
            return f"Username Error: {UsernameTooShort(username)}"
        except UsernameTooLong:
            return f"Username Error: {UsernameTooLong(username)}"
        except PasswordMissingCharacter:
            return f"Passward Error: {PasswordMissingCharacter(password)}"
        except PasswordTooLong:
            return f"Passward Error: {PasswordTooLong(password)}"
        except PasswordTooShort:
            return f"Passward Error: {PasswordTooShort(password)}"

        else:
            return "OK"

    def main():
        print(check_input("Yv56Y", "tttttttTttt"))

    main()


if __name__ == '__main__':
    user_name_pass_ward()
