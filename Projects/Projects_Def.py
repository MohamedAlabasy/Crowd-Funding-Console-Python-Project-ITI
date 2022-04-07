import os
from . import Product_Validation  # because iam run from welcome
from Database import Database_CRUD
import current_login_user

current_user = current_login_user.get_user()


def create_project():
    print("""
    +=======================================================================================+
    |           You Have Chosen to Create Project Please Enter Your Data 😁                 |
    +=======================================================================================+
    """)
    try:
        product_title = input("Enter Product Your Title : ")
        while not Product_Validation.title_validation(product_title):
            product_title = input("invalid Title Please Enter it Again : ")

        product_details = input("Enter Your Product Details : ")
        while not Product_Validation.details_validation(product_details):
            product_details = input("invalid Details Please Enter it Again : ")

        product_total_target = input("Enter Your Product Total Target : ")
        while not Product_Validation.total_target_validation(product_total_target):
            product_total_target = input(
                "invalid Total Target Please Enter it Again : ")

        product_start_time = input("Enter Your Product Start Time : ")
        while not Product_Validation.start_time_validation(product_start_time):
            product_start_time = input(
                "invalid Start Time Please Enter it Again : ")

        product_end_time = input("Enter Your Product End Time : ")
        while not Product_Validation.end_time_validation(product_end_time):
            product_end_time = input(
                "invalid End Time Please Enter it Again : ")

    except Exception as e:
        print(f"""
    +=======================================================================================+
    | Exception 😤 : {e}                                                                    |
    +=======================================================================================+
            """)
    else:
        Database_CRUD.create_project(
            id=0,
            title=product_title.lower().strip(),
            details=product_details.lower().strip(),
            total_target=product_total_target.strip(),
            start_time=product_start_time.strip(),
            end_time=product_end_time.strip(),
            user_id=current_user["id"],
        )
        all_projects()


def edit_projects():
    print("""
    +=======================================================================================+
    |               You Have Chosen to Edit Please Enter Your Data 😁                       |
    +=======================================================================================+
    """)
    try:
        product_title = input("Enter Your product title update it : ")
        while not Product_Validation.title_validation(product_title):
            product_title = input("invalid title_validation : ")

        if not Database_CRUD.search_project(product_title, current_user["id"]):
            all_projects()
    except Exception as e:
        print(f"""
    +=======================================================================================+
    | Exception 😤 : {e}                                                                    |
    +=======================================================================================+
            """)
    else:
        print("""
    +=======================================================================================+
    |                           Select What You Want to Edit in 🧐                          |
    +=======================================================================================+
    |                                       1.Title                                         |
    |                                       2.Details                                       |
    |                                       3.Total Target                                  |
    |                                       4.Start Time                                    |
    |                                       5.End Time                                      |
    |                                       6.Back                                          |
    +=======================================================================================+
        """)

    edit_select = input("Enter Your Choice : ")
    while not edit_select:
        print(f"""
    +=======================================================================================+
    | Exception 😤 : {e}                                                                    |
    +=======================================================================================+
            """)
        edit_select = input("Enter Your Choice : ")

    if edit_select.isdigit() and edit_select in ["1", "2", "3", "4", "5", "6"]:
        # os.system("cls")  # to clear the screen
        _edit_select = int(edit_select)
        if _edit_select == 1:
            edit_words = "title"
        elif _edit_select == 2:
            edit_words = "details"
        elif _edit_select == 3:
            edit_words = "total_target"
        elif _edit_select == 4:
            edit_words = "start_time"
        elif _edit_select == 5:
            edit_words = "end_time"
        elif _edit_select == 6:
            return all_projects()
        new_data = input(f"Enter Your {edit_words} : ")
        Database_CRUD.edit_projects(
            product_title, edit_words, new_data, current_user["id"])
    else:
        print("""
    +=======================================================================================+
    |                   You Must Enter Only 1 or 2 or 3 or 4 or 5 or 6 👌                   |
    +=======================================================================================+
""")
    all_projects()


def delete_project():
    print("""
    +=======================================================================================+
    |               You Have Chosen to Delete Please Enter Your Data 😁                     |
    +=======================================================================================+
    """)
    try:
        product_title = input("Enter Your product title to delete it : ")
        while not Product_Validation.title_validation(product_title):
            product_title = input("invalid title_validation : ")

        if not Database_CRUD.search_project(product_title, current_user["id"]):
            all_projects()

    except Exception as e:
        print(f"""
    +=======================================================================================+
    | Exception 😤 : {e}                                                                    |
    +=======================================================================================+
            """)
    else:
        Database_CRUD.delete_project(
            product_title.lower().strip(), current_user["id"])
        all_projects()


def search_project():
    try:
        product_title = input("Enter Your product title to search it : ")
        while not Product_Validation.title_validation(product_title):
            product_title = input("invalid title_validation : ")
        if Database_CRUD.search_project(product_title, current_user["id"]):
            project_data = Database_CRUD.search_project(
                product_title, current_user["id"])
            print("=======================================================================================================================")
            print("| {:<5} | {:<15} | {:<20} | {:<20} | {:<20} | {:<20} |".format(
                "ID", "Title", "Details", "Total Target", "Start Time", "End Time"))
            print("=======================================================================================================================")
            print(
                "| {:<5} | {:<15} | {:<20} | {:<20} | {:<20} | {:<20} |".format(project_data["id"], project_data["title"], project_data["details"], project_data["total_target"], project_data["start_time"], project_data["end_time"]))
            print("=======================================================================================================================")
            all_projects()
        else:
            all_projects()

    except Exception as e:
        print(f"""
    +=======================================================================================+
    | Exception 😤 : {e}                                                                    |
    +=======================================================================================+
            """)
    else:
        Database_CRUD.search_project(product_title, current_user["id"])


def all_projects():
    all_projects_data = Database_CRUD.all_projects()
    if len(all_projects_data) == 0:
        print("""
    +=======================================================================================+
    |                           There ara no projects to show 😢                            |
    +=======================================================================================+
            """)
    else:
        print("=======================================================================================================================")
        print("| {:<5} | {:<15} | {:<20} | {:<20} | {:<20} | {:<20} |".format(
            "ID", "Title", "Details", "Total Target", "Start Time", "End Time"))
        print("=======================================================================================================================")
        for row in all_projects_data:
            print(
                "| {:<5} | {:<15} | {:<20} | {:<20} | {:<20} | {:<20} |".format(row["id"], row["title"], row["details"], row["total_target"], row["start_time"], row["end_time"]))
        print("=======================================================================================================================")
    print("""
    +=======================================================================================+
    |                           Welcome to the Products Program 😎                          |
    +=======================================================================================+
    |                                   1.Create Project                                    |
    |                                   2.Edit Project                                      |
    |                                   3.Delete Project                                    |
    |                                   4.Search on Projects                                |
    |                                   5.Exit Project                                      |
    +=======================================================================================+
    """)
    user_select = input("Enter Your Choice : ")
    while not user_select:
        print("""
    +=======================================================================================+
    |               You can't enter empty data please enter only Numbers 😢                 |
    +=======================================================================================+
            """)
        user_select = input()

    if user_select.isdigit() and user_select in ["1", "2", "3", "4", "5"]:
        os.system("cls")  # to clear the screen
        _user_select = int(user_select)
        if _user_select == 1:
            create_project()
        elif _user_select == 2:
            edit_projects()
        elif _user_select == 3:
            delete_project()
        elif _user_select == 4:
            search_project()
        elif _user_select == 5:
            print("""
    +=======================================================================================+
    |                   Exit Successfully, We Hope You Will Come Back Soon 🥺               |
    +=======================================================================================+
            """)
            return current_login_user.set_user()
    else:
        print("""
    +=======================================================================================+
    |                       You Must Enter Only 1 or 2 or 3 or 4 or 5 👌                    |
    +=======================================================================================+
        """)
        all_projects()
