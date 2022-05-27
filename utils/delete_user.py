from click import option
import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/users"


def get_user(pk):
    url= "%s/%s" % (URL, pk)
    response  = requests.get(url)
    if response.status_code  == 200:
       pprint(response.json())
    else:
        print("Something went wrong retrieving user.")

def delete_user(pk):
    url= "%s/%s" % (URL, pk)
    response  = requests.get(url)
    if response.status_code  == 204:
       print("User successfully deleted.")
    else:
        print("Something went wrong deleting user.")       

if __name__ == "__main__":
    print("DELETE A USER")
    print("_" * 50)
    user_id = input("Type in the target user's ID:")
    
    
    get_user(user_id)
    option = input ("[Y/N] : ")
    if option == "Y" or option == "y":
        delete_user(user_id)
    else:
        print("Something went wrong deleting user.")    

