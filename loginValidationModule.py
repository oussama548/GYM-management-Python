from DB import DataBase

class validLogin: #object responsible for validating the input data
    def __init__(self):
        self.db=DataBase() #now we have an object that handles the database (self.db.cursor)
        

    def validData(self,mail:str,password:str)->bool:
         #1- retrieve data->SQL command
         try:
             query = "SELECT * FROM Admin WHERE Email = %s AND Password = %s"  #String formatting: to let sql know
                                                                               #that mail and psswd are strings
             self.db.cursor.execute(query, (mail, password))
             result= self.db.cursor.fetchone() is not None
             self.db.CloseDb()
             return result
         except Exception as e:
             print(f"Error in db connection {e}")
