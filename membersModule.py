from DB import DataBase
import re #for regex
from ValidationModule import valid
from PySide6.QtWidgets import QMessageBox,QWidget
from datetime import date
class Members:
    def __init__(self):
        self.db=DataBase()
        self.Valid=valid()

    
    #########ADD MEMBER###########
    ##############################
    def addMember(self,F_name:str,L_name:str,age:str,gender:str,mail:str,phone:str,sessions:str,duration:str):
        if(self.Valid.validInformation(F_name,L_name,age,gender,mail,phone,sessions)):
            #we add the data to the DB
            startdate=date.today() #1-start date
            try:
                command="""INSERT INTO Member 
                           (FirstName,LastName,Age,Gender,Email,Phone,StartDate,Duration,Coach,sessionsperweek) 
                           VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                        """#SessionsPerWeek,Duration
                values=(F_name,L_name,age,gender,mail,phone,startdate,duration,None,sessions) #sessions,duration
                self.db.cursor.execute(command,values) #DBMS will store the entered data
                self.db.commitChange()
            except Exception as e:
                print(f"Exception occured: {e}")
        else:#not valid data
            widg=QWidget()
            QMessageBox.warning(widg,"Invalid member data","Please ensure valid user data")



    #######SEARCH MEMBER############
    ################################
    def searchMember(self,filter:str,data:str)->list[tuple]: #1-fetch from DB   2-return the list of rows
        if(filter=="First Name"):
            command="""SELECT * FROM Member
                    WHERE firstname = %s"""
        elif(filter=="Second Name"):
            command="""SELECT * FROM Member
                    WHERE lastname = %s"""
        elif(filter=="Phone Number"):
            command="""SELECT * FROM Member
                    WHERE phone = %s"""
        elif(filter=="Email"):
            command="""SELECT * FROM Member
                    WHERE email = %s"""

        try:
            queryVal=(data,)
            self.db.cursor.execute(command,queryVal)
            print("command executes successfully")
            values=self.db.cursor.fetchall()
            return values
        except Exception as e:
            print(f"error: {e}")


    #########UPDATE MEMBER#########
    ###############################  
    def updateMember(self,ID:str,F_name:str,L_name:str,age:str,gender:str,mail:str,phone:str,sessions:str,duration:str)->None:
        print(ID,F_name,L_name,age,gender,mail,phone,sessions,duration)
        if(self.Valid.validInformation(F_name,L_name,age,gender,mail,"0"+phone,sessions)):
            try:
                #1-add to the DB:
                command="""UPDATE Member SET
                           firstname=%s,
                           lastname=%s,
                           age=%s,
                           gender=%s,
                           email=%s,
                           phone=%s,
                           sessionsperweek=%s,
                           duration=%s
                           WHERE id=%s;
                   """
                values=(F_name,L_name,age,gender,mail,phone,sessions,duration,ID)
                self.db.cursor.execute(command,values)
                self.db.commitChange()
            except Exception as e:
                print(f"Exception: {e}")
        else:#not valid data
            widg=QWidget()
            QMessageBox.warning(widg,"Invalid member data","Please ensure valid user data")           
                    

    #########DELETE MEMBER#########
    ###############################
    def deleteMember(self,ID):
        command="""DELETE FROM Member
                   WHERE id=%s """
        id=(ID,)
        try:
            self.db.cursor.execute(command,id)
            self.db.commitChange()
            print("User deleted succefully")
        except Exception as e:
            print(f"Exception: {e}")


    ########ASSIGN COACH############
    ################################
    def assignCoach(self,memberId:str,coachId:str)->bool:
        command="""UPDATE Member 
                   SET coach=%s
                   WHERE id=%s;"""
        values=(coachId,memberId)
        try:
            self.db.cursor.execute(command,values)
            self.db.commitChange()
            return True
        except Exception as e:
            print(f"Exception: {e}")
            return False
