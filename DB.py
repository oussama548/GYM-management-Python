# This Python file uses the following encoding: utf-8
import psycopg2

class DataBase:
    def __init__(self):
        self.connection=None
        self.cursor=None

    def dbConnect(self):
        try:
            self.connection=psycopg2.connect(dbname="GYM_manager",
                                         user="postgres",
                                         password="daachipostgre@24",
                                         host="localhost",
                                         port=5432)
            print("DB connection succeded")
        except Exception as e:
            print(f"Error in connecting to the DB: {e}")
        try:    
            self.cursor=self.connection.cursor()
            print("Cursor created succesfuly")
        except Exception as e:
            print(f"cursor not made : {e}")

    def commitChange(self):
        if(self.connection):
            self.connection.commit()

    def CloseDb(self):
        try:
            self.cursor.close()
            print("db closed")
        except(Exception):
            print("db not closed")
 
  