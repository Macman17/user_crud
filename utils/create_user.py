from distutils.command.build_scripts import first_line_re

import requests

URL = "http://127.0.0.1:5000/users"
USER_TEMPLATE= {
    "first_name": "John",
    "last_name": "Doe",
    "hobbies": "Hiking"

}

def create_user(first_name, last_name, hobbies):
    user_data = USER_TEMPLATE
    user_data["first_name"] = first_name
    user_data["last_name"] = last_name
    user_data["hobbies"] = hobbies
    response = requests.post(URL, json=user_data)
    if response.status_code == 204:
        print("User successfully created")
    else:
        print("Something went wrong while trying to create a user")  

if __name__ == "__main__":
    print("CREATE A USER")
    print("_______________")
    fname = input("First Name: ")
    lname = input("Last Name: ")
    hobbies = input("Hobbies: ")
    create_user(fname, lname, hobbies)



  
     


