import os
import datetime
import re

date_regex = r'^(0?[1-9]|[12][0-9]|3[01])[\/\-](0?[1-9]|1[012])[\/\-]\d{4}$'


def title_validation(_title):
    if len(_title) > 3 and len(_title) < 15 and _title.isalpha():
        return True
    else:
        os.system("cls")
        return False


def details_validation(_details):
    if len(_details) > 3 and _details.isalpha():
        return True
    else:
        os.system("cls")
        return False


def total_target_validation(_total_target):
    if len(_total_target) > 3 and len(_total_target) < 20 and _total_target.isdigit():
        return True
    else:
        os.system("cls")
        return False


def start_time_validation(_start_time):
    print(_start_time)
    if len(_start_time) > 3 and re.fullmatch(_start_time, date_regex) and check_date(_start_time):
        return True
    else:
        os.system("cls")
        return False


def end_time_validation(_end_time):
    if len(_end_time) > 3 and len(_end_time) < 20 and re.fullmatch(_end_time, date_regex) and check_date(_end_time):
        return True
    else:
        os.system("cls")
        return False


def check_date(time):
    today = datetime.date.today().strftime("%d-%m-%Y")
    start_time = datetime.datetime.strptime(today, '%d-%m-%Y')
    end_time = datetime.datetime.strptime(time, '%d-%m-%Y')
    if start_time > end_time:
        return False
    elif start_time < end_time:
        return True
