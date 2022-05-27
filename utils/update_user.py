import requests



URL = "http://127.0.0.1:5000/users"
USER_TEMPLATE= {
    
    "first_name": "John",
    "last_name": "Doe",
    "hobbies": "Hiking"

}

def get_user(pk):
    url= "%s/%s" % (URL, pk)
    response  = requests.get(url)
    print(response.json())

def update_user(pk, first_name, last_name, hobbies ):
    url= "%s/%s" % (URL, pk)
    user_data = USER_TEMPLATE
    user_data["first_name"] = first_name
    user_data["last_name"] = last_name
    user_data["hobbies"] = hobbies
    response2 = requests.put(url, json= user_data)
    if response2.status_code == 204:
        print("User successfully updated")
        
    else:
        print("Something went wrong while trying to update a user") 
    

if __name__ == "__main__":
    target_id = input("Please enter user's ID: ")
    print("Would you like to update the user shown below?")
    get_user(target_id)
    option = input ("[Y/N] : ")
    
    if option == "Y" or option == "y":

        fname = input("First Name: ")
        lname = input("Last Name: ")
        hobbies = input("Hobbies: ") 
        print("-----------")
        update_user(target_id, fname, lname, hobbies) 
    else:
        print("Something went wrong deleting user.")
    

     