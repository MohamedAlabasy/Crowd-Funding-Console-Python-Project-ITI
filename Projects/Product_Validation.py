import os


def title_validation(_title):
    if len(_title) > 3:
        return True
    else:
        os.system("cls")
        return False


def details_validation(_details):
    if len(_details) > 3:
        print("true")
        return True
    else:
        os.system("cls")
        return False


def total_target_validation(_total_target):
    if len(_total_target) > 3:
        print("true")
        return True
    else:
        os.system("cls")
        return False


def start_time_validation(_start_time):
    if len(_start_time) > 3:
        print("true")
        return True
    else:
        os.system("cls")
        return False


def end_time_validation(_end_time):
    if len(_end_time) > 3:
        return True
    else:
        os.system("cls")
        return False
