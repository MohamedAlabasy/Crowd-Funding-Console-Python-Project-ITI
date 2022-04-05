import os


def name_validation(_name):
    if len(_name) > 3:
        return True
    else:
        os.system("cls")
        return False


def email_validation(_email):
    if len(_email) > 3:
        print("true")
        return True
    else:
        os.system("cls")
        return False


def password_validation(_password):
    if len(_password) > 3:
        print("true")
        return True
    else:
        os.system("cls")
        return False


def confirm_password_validation(_password, _confirm_password):
    if _password == _confirm_password:
        print("true")
        return True
    else:
        os.system("cls")
        return False


def phone_validation(_phone):
    if len(_phone) > 3:
        print("true")
        return True
    else:
        os.system("cls")
        return False


def login_validation(_email, _password):
    if len(_email) > 3:
        return True
    else:
        os.system("cls")
        return False
