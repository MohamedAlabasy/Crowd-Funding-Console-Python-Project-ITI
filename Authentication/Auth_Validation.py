import os
import re

email_regex = r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+'
phone_regex = r'^01[0125][0-9]{8}$'


def name_validation(_name):
    if len(_name) > 3 and _name.isalpha():
        return True
    else:
        os.system("cls")
        return False


def email_validation(_email):
    if len(_email) > 4 and re.fullmatch(email_regex, _email):
        return True
    else:
        os.system("cls")
        return False


def password_validation(_password):
    if len(_password) > 3:
        return True
    else:
        os.system("cls")
        return False


def confirm_password_validation(_password, _confirm_password):
    if _password == _confirm_password:
        return True
    else:
        os.system("cls")
        return False


def phone_validation(_phone):
    if len(_phone) == 11 and re.fullmatch(phone_regex, _phone):
        return True
    else:
        os.system("cls")
        return False


def login_validation(_email):
    if len(_email) > 3 and re.fullmatch(email_regex, _email):
        return True
    else:
        os.system("cls")
        return False
