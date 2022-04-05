import os
import Authentication.Auth_Def as Auth_Def


print("""
+=======================================================================================+
|                           Welcome to the Products Program 😎                          |
+=======================================================================================+
|                                   1.Login                                             |
|                                   2.Regestration                                      |
|                                   3.Exit Project                                      |
+=======================================================================================+
""")

user_select = input("Enter Your Choice : ")
while not user_select:
    print("""
+=======================================================================================+
|               You can't enter empty data please enter only Numbers 😢                 |
+=======================================================================================+
""")
    user_select = input("Enter Your Choice : ")

if user_select.isdigit() and user_select in ["1", "2", "3"]:
    os.system("cls")  # to clear the screen
    Auth_Def.authentication(user_select)
else:
    print("""
+=======================================================================================+
|                           You Must Enter Only 1 or 2 or 3 👌                          |
+=======================================================================================+
""")
