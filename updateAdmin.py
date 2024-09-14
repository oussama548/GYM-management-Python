from DB import DataBase
from ValidationModule import valid

class validUpdate:
    def __init__(self):
        self.db=DataBase()
        self.Valid=valid()

    def updatePassword(self,currPasswd:str,newPasswd:str)->tuple:
        #1-identify the admin
        searchSql="""SELECT * FROM Admin
                    WHERE password=%s;"""
        currPassword=(currPasswd,)
        try:
            self.db.cursor.execute(searchSql,currPassword)
            if(self.db.cursor.fetchone() is None): #invalid user
                return (False,"incorrect password")
        except Exception as e:
            print(f"Error: {e}")
            return (False,"Unable to identify the Admin,please try again")
        
        #2-valid the password
        if(not self.Valid.validPassword(newPasswd)):
            return (False,"invalid password")
        #3-update the password
        command="""UPDATE Admin
                   SET password=%s
                   WHERE password=%s;"""
        vals=(newPasswd,currPasswd)
        try:
           self.db.cursor.execute(command,vals)
           self.db.commitChange()
           return (True,"Updated successfully")
        except Exception as e:
            print(f"exception: {e}")
            return (False,"error in updating password")


    def updateEmail(self,currMail:str,newMail:str)->tuple:
        #1-identify the admin
        searchSql="""SELECT * FROM Admin
                    WHERE email=%s;"""
        currPassword=(currMail,)
        try:
            self.db.cursor.execute(searchSql,currPassword)
            if(self.db.cursor.fetchone() is None): #invalid user
                return (False,"incorrect email")
        except Exception as e:
            print(f"exception: {e}")
            return (False,"Unable to identify the admin,please try again")
        #2-valid the email
        if(not self.Valid.valiEmail(newMail)):
            return (False,"invalid email,please respect the constraints")
        #3-update the email
        command="""UPDATE Admin
                   SET email=%s
                   WHERE email=%s;"""
        vals=(newMail,currMail)
        try:
           self.db.cursor.execute(command,vals)
           self.db.commitChange()
           return (True,"Updated successfully")
        except Exception as e:
            print(f"exception: {e}")
            return (False,"error in updating email")
            


