
import re

class valid:
    def __init__(self):
        pass

    def valiEmail(self,mail:str)->bool:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        # Check if the email matches the pattern
        if re.match(pattern, mail):
            return True
        return False    

    def validGender(self,gen:str)->bool:
        if(gen.upper()=="M" or gen.upper()=="F"):
            return True
        else:
            return False

    def validNmber(self,num:str)->bool:
        if(len(num)==10 and num.isnumeric() and num[0]=="0" and num[1] in ["5","6","7"] ):
            return True
        else:
            return False

    def validAge(self,age:str):
        Age=int(age)
        if(Age>10 and Age<100):
            return True
        else:
            return False
    
    def validSessions(self,sess:str):
        Sessions=int(sess)
        if(Sessions>=1 and Sessions<=6):
            return True
        else:
            return False
    
    def validInformation(self,F_name:str,L_name:str,age:str,gender:str,mail:str,phone:str,sessions:str)->bool:
        return self.validAge(age) and self.validGender(gender)  and self.validNmber(phone) and self.valiEmail(mail) and self.validSessions(sessions) 

    def validPassword(self,psswd:str)->bool:
        if(len(psswd)<8 or psswd.isalpha()): #1-less than 8 chars   2-contains only alpha-numeric chars
            return False
        else:
            return True