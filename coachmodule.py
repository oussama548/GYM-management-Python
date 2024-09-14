
from ValidationModule import valid
from DB import DataBase
from PySide6.QtWidgets import QMessageBox,QWidget


class coach:
    def __init__(self):
        self.db=DataBase()
        self.Valid=valid()

    
    #######ADD COACH############
    ############################
    def addCoach(self,F_name:str,L_name:str,age:str,mail:str,phone:str,dayWeek:str,pay:str)->bool:
        if(self.Valid.validInformation(F_name,L_name,age,"M",mail,phone,dayWeek)):
            command="""
                    INSERT INTO coach(firstname,lastname,age,email,phone,daysperweek,salary)
                    VALUES(%s,%s,%s,%s,%s,%s,%s)
             """
            values=(F_name,L_name,age,mail,phone,dayWeek,pay)
            try:
                self.db.cursor.execute(command,values)
                self.db.commitChange()
                return True
            except Exception as e:
                print(f"Exception: {e}")
                return False

        else:
            widget=QWidget()
            QMessageBox.warning(widget,"Invalid data","Please ensure valid input")
            return False
            

    ########SEARCH COACH###########
    ###############################
    def searchCoach(self,filter:str,value:str)->list[tuple]:
        if(filter=="First Name"):
            command="""SELECT * FROM coach
                    WHERE firstname = %s"""
        elif(filter=="Second Name"):
            command="""SELECT * FROM coach
                    WHERE lastname = %s"""
        elif(filter=="Phone Number"):
            command="""SELECT * FROM coach
                    WHERE phone = %s"""
        elif(filter=="Email"):
            command="""SELECT * FROM coach
                    WHERE email = %s"""
        val=(value,)
        try:
            self.db.cursor.execute(command,val)
            data=self.db.cursor.fetchall()
            return data
        except Exception as e:
            print(f"exception: {e}")

    def searchTrainees(self,id:str)->list[tuple]:
        command="""SELECT Member.firstname,Member.lastname 
                   FROM Member JOIN coach 
                   ON Member.coach=coach.coach_id
                   AND coach.coach_id=%s;"""
        ID=(id,)
        try:
            self.db.cursor.execute(command,ID)
            trainees=self.db.cursor.fetchall()
            return trainees
        except Exception as e:
            print(f"Exception: {e}")
            return None


    #########UPDATE COACH###########
    ################################
    def updateCoach(self,id:str,updatedData:tuple)->bool:
        #1-check for validation
        if(self.Valid.validInformation(updatedData[0],updatedData[1],updatedData[2],"M",updatedData[3],"0"+updatedData[4],updatedData[5])):
            command="""UPDATE coach SET
                       firstname=%s,
                       lastname=%s,
                       age=%s,
                       email=%s,
                       phone=%s,
                       daysperweek=%s,
                       salary=%s
                       WHERE coach_id=%s
            """
            values=updatedData.__add__((id,))
            try:
                self.db.cursor.execute(command,values)
                self.db.commitChange()
                return True
            except Exception as e:
                print(f"Exception: {e}")
                return False
        else:
            widget=QWidget()
            QMessageBox.warning(widget,"Invalid information","Please ensure valid information")
            return False


    #########DELETE COACH###########
    ################################
    def deleteCoach(self,id):
        command="""DELETE FROM coach
                   WHERE coach_id=%s;"""
        value=(id,)
        try:
            self.db.cursor.execute(command,value)
            self.db.commitChange()
        except Exception as e:
            print(f"exception: {e}")
        
                  
