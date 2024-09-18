import json

class Database:
    def insert(self,name,email,age,education,year,clg,day):
        with open('members.json','r') as rf:
            users = json.load(rf)
        if email or day in users:
            return 0
        else:
            users[email] = [name,email,age,education,year,clg,year,day]
            with open("members.json",'w') as wf:
                json.dump(users,wf,indent=4)
                return 1
