import json
from operator import index
from textwrap import indent
import current_login_user

user_database_path = "Database/users_db.json"
projects_database_path = "Database/projects_db.json"


def find_user(_email):
    try:
        with open(user_database_path, "r+") as file:
            database = json.load(file)
            for data in database:
                if data["email"] == _email:
                    current_login_user.set_user(
                        id=data["id"],
                        first_name=data["first_name"],
                        last_name=data["last_name"],
                        email=data["email"],
                        password=data["password"],
                        phone=data["phone"],
                    )

    except Exception as e:
        print(f"""
+=======================================================================================+
|                                   Exception 😤 : {e}                                  |
+=======================================================================================+
            """)
    finally:
        file.close()


def add_user(**kwargs):
    try:
        with open(user_database_path, "r+") as file:
            database = json.load(file)

            # to add ID
            if len(database) > 0:
                id = len(database)+1
            else:
                id = 1
            kwargs.update({"id": id})

            database.append(kwargs)
            file.seek(0)
            json.dump(database, file)

    except Exception as e:
        print(f"""
+=======================================================================================+
|                                   Exception 😤 : {e}                                  |
+=======================================================================================+
            """)
    finally:
        file.close()


def all_projects():
    try:
        with open(projects_database_path, "r") as file:
            database = json.load(file)
            return database

    except Exception as e:
        print(f"""
+=======================================================================================+
|                                   Exception 😤 : {e}                                  |
+=======================================================================================+
            """)
    finally:
        file.close()


def create_project(**kwargs):
    try:
        with open(projects_database_path, "r+") as file:
            database = json.load(file)

            # to add ID
            if len(database) > 0:
                id = len(database)+1
            else:
                id = 1
            kwargs.update({"id": id})

            database.append(kwargs)
            file.seek(0)
            json.dump(database, file)

    except Exception as e:
        print(f"""
+=======================================================================================+
|                                   Exception 😤 : {e}                                  |
+=======================================================================================+
            """)
    finally:
        file.close()


def delete_project(product_title):
    try:
        database = json.load(open(projects_database_path))
        print(database)
        with open(projects_database_path, "w") as file:
            for index, data in enumerate(database):
                if data["title"] == product_title:
                    del database[index]
                    file.seek(0)
                    json.dump(database, file)
                break
            else:
                print("""
+=======================================================================================+
|                           This Project Doesn't Exist 😥                               |
+=======================================================================================+
            """)
    except Exception as e:
        print(f"""
+=======================================================================================+
|                                   Exception 😤 : {e}                                  |
+=======================================================================================+
            """)
    finally:
        file.close()


def edit_projects(product_title, edit_words, new_data):
    try:
        database = json.load(open(projects_database_path))
        with open(projects_database_path, "w") as file:
            for index, data in enumerate(database):
                if data["title"] == product_title:
                    database[index][edit_words] = new_data
                    file.seek(0)
                    json.dump(database, file)
                    print(database)
                break
            else:
                print("""
+=======================================================================================+
|                           This Project Doesn't Exist 😥                               |
+=======================================================================================+
            """)
    except Exception as e:
        print(f"""
+=======================================================================================+
|                                   Exception 😤 : {e}                                  |
+=======================================================================================+
            """)
    finally:
        file.close()


def search_project(product_title):
    try:
        with open(projects_database_path, "r") as file:
            database = json.load(file)
            for data in database:
                if data["title"] == product_title:
                    break
            else:
                print("""
+=======================================================================================+
|                           This Project Doesn't Exist 😥                               |
+=======================================================================================+
            """)
    except Exception as e:
        print(f"""
+=======================================================================================+
|                                   Exception 😤 : {e}                                  |
+=======================================================================================+
            """)
    finally:
        file.close()
