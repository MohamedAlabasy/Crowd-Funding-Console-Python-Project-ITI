current_login_user = {}


def set_user(**kwargs):
    current_login_user.update(kwargs)


def get_user():
    return current_login_user
