from DB import DataBase
from ValidationModule import valid
from PySide6.QtWidgets import QMessageBox,QWidget
from datetime import date

class machine:
    def __init__(self):
        self.db=DataBase()
        self.Valid=valid()

    
    ##########Store the data into the DB##########

    def storeMachineData(self,name:str,cost:str,description:str,img:bytes)->bool:
        bringDate=date.today()
        #1-store the data
        command="""INSERT INTO equipement (name,description,cost,bringdate,image)
                   VALUES (%s,%s,%s,%s,%s)"""
        values=(name,description,cost,bringDate,img)
        if(int(cost)>0):
            try:
                self.db.cursor.execute(command,values)
                self.db.commitChange()
                return True 
            except Exception as e:
                print(f"Exception: {e}")
                return False
        else:
            return False

    ###########Search for a machine##################
    def searchMachine(self,name:str)->list[tuple]:
        command="""SELECT * FROM equipement
                   WHERE name=%s;"""
        value=(name,)
        try:
            self.db.cursor.execute(command,value)
            data=self.db.cursor.fetchall()
            return data
        except Exception as e:
            print(f"Exception: {e}")
            return []


    ######DELETE a machine##################
    def deleteMachine(self,id:str)->bool:

        command="""DELETE FROM equipement
                   WHERE id=%s;"""
        value=(id,)
        try:
            self.db.cursor.execute(command,value)
            self.db.commitChange()
            print("machine is deleted")
        except Exception as e:
            print(f"exception: {e}")

