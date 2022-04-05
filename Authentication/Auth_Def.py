import os
from . import Auth_Validation  # because iam run from welcome
from Database import Database_CRUD
import current_login_user
from Projects import Projects_Def


def login():
    print("""
+=======================================================================================+
|                   You Have Chosen to Login Please Enter Your Data 😁                  |
+=======================================================================================+
    """)
    try:
        login_email = input("Enter Your Email  : ")
        login_password = input("Enter Your Password : ")

        while not Auth_Validation.login_validation(login_email, login_password):
            print("""
+=======================================================================================+
|                   invalid Email or Password Enter it Aging 😢                         |
+=======================================================================================+
            """)
            login_email = input("Enter Your Email  : ")
            login_password = input("Enter Your Password : ")

    except Exception as e:
        print(e)
    else:
        Database_CRUD.find_user(login_email.lower())
        if len(current_login_user.get_user()) != 0:
            if current_login_user.get_user()["password"] == login_password:
                print("""
+=======================================================================================+
|                                   welcome back 🤩                                     |
+=======================================================================================+
                """)
                Projects_Def.all_projects()
            else:
                print("""
+=======================================================================================+
|                                   Wrong password 🤥                                   |
+=======================================================================================+
                """)
        else:
            os.system("cls")
            print("""
+=======================================================================================+
|                           There is No User With this Email 😑                         |
+=======================================================================================+
            """)


def registration():
    print("""
+=======================================================================================+
|               You Have Chosen to Register Please Enter Your Data 😁                   |
+=======================================================================================+
    """)
    try:
        first_name = input("Enter Your First Name : ")
        # make condition false
        while not Auth_Validation.name_validation(first_name):
            first_name = input("Invalid First Name Please Enter it Again : ")

        last_name = input("Enter Your Second Name : ")
        while not Auth_Validation.name_validation(last_name):
            last_name = input("Invalid Second Name Please Enter it Again : ")

        user_email = input("Enter Your Email : ")
        while not Auth_Validation.email_validation(user_email):
            user_email = input("Invalid Email Please Enter it Again : ")

        user_password = input("Enter Your Password  : ")
        while not Auth_Validation.password_validation(user_password):
            user_password = input("Invalid Password Please Enter it Again : ")

        confirm_password = input("confirm Your Password  : ")
        while not Auth_Validation.confirm_password_validation(user_password, confirm_password):
            confirm_password = input(
                "password don't match Please Enter it Again : ")

        mobile_phone = input("Enter Your phone Number : ")
        while not Auth_Validation.phone_validation(mobile_phone):
            mobile_phone = input(
                "Invalid Phone Number Please Enter it Again : ")
    except Exception as e:
        print(e)
    else:
        Database_CRUD.add_user(
            id=0,
            first_name=first_name.lower().strip(),
            last_name=last_name.lower().strip(),
            email=user_email.lower().strip(),
            password=user_password.strip(),
            phone=mobile_phone.strip(),
        )


def authentication(_user_select):
    user_select = int(_user_select)
    if user_select == 1:
        login()
    elif user_select == 2:
        registration()
    elif user_select == 3:
        current_login_user.set_user()
        print("""
+=======================================================================================+
|                   Exit Successfully, We Hope You Will Come Back Soon 🥺               |
+=======================================================================================+
            """)
        os.system("exit")
