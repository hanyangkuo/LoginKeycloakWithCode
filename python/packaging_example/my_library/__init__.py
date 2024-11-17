import requests
import os
import jwt 

class Postman:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getResponse(self):
        headers = {
            "Authorization": "Bearer YOUR_ACCESS_TOKEN",
            "Accept": "application/json"
        }
        response = requests.get("https://jsonplaceholder.typicode.com/todos/1", headers=headers)
        return response.text
    

    def __writeResponse(self, text):
        basepath = os.path.join(os.getenv("LOCALAPPDATA"),"testproject")
        filepath = os.path.join(basepath, "token")
        print(filepath)
        if not os.path.exists(basepath):
            os.makedirs(basepath)
        with open(filepath, 'w') as f:
            f.write(text)

    def __readResponse(self):
        basepath = os.path.join(os.getenv("LOCALAPPDATA"),"testproject")
        filepath = os.path.join(basepath, "token")
        print(filepath)
        if os.path.exists(basepath):
            with open(filepath, 'r') as f:
                return f.readlines()

def verifyToken(token):
    try:  
        result = jwt.decode(token, algorithms=["RS256"],options={"verify_signature": False, "verify_exp": True})
        print(result)
        return True
    except:
        return False

if __name__ == '__main__':
    postman = Postman("Young", "18")
    print(postman.getResponse())

    token = "eyJhbGciOiJIUzUxMiIsInR5cCIgOiAiSldUIiwia2lkIiA6ICI2ZDkxODNkMC0wZWJlLTQyMDEtYWY5MC0yNTMzNmI1ZjEwNTIifQ.eyJleHAiOjE3MzE4NTQ0MTUsImlhdCI6MTczMTg1NDI5NSwianRpIjoiNWI5OTQyZDQtNTJkOC00ODBmLTkwMjgtNDAxZjc2NjM3ZmVmIiwiaXNzIjoiaHR0cDovL2xvY2FsaG9zdDo4MDgwL3JlYWxtcy90ZXN0Iiwic3ViIjoiODE0MGQ3ZmYtNjFhMC00MzA0LWIyNmItOTViOWRmNTE3YTY4IiwidHlwIjoiU2VyaWFsaXplZC1JRCIsInNpZCI6IjY2MzZjMmQ5LWEzODQtNDIzMi04YTkxLThiOGMyZjkxYzFlMSIsInN0YXRlX2NoZWNrZXIiOiI0TnI2REpPQ0YtUm43NVJwUzdZQlREMERlTzlFalZLbmZFbTJHN21OcHRBIn0.Dpzb-3mNX4C5aXmcRpev0W2LF_h7hnH2FOhmvMYObL37gdooah9Qq9_Bn7t6yvPSyYtmSAsOCTCYMbBt7FJhrg"
    result = jwt.decode(token, algorithms=["RS256"],options={"verify_signature": False, "verify_exp": True})
    print(result)