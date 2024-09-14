# This Python file uses the following encoding: utf-8
import sys
import base64
from PySide6.QtWidgets import QApplication, QMainWindow,QMessageBox,QTableWidgetItem,QFileDialog,QLabel
from PySide6.QtGui import QPixmap
from PyQt6.QtCore import Qt





# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainPage

#databases:
#from DB import DataBase ->commented until we need it

#Admin validation:
from loginValidationModule import validLogin

#members attribute -> used to handle members:1-add 2-update 3-delete 4-search /  and connecting to the DB
from membersModule import Members           
from coachmodule import coach
from equipementModule import machine
from updateAdmin import validUpdate



#main UI:
class MainPage(QMainWindow,Ui_MainPage): #DB connection is made in the eventListener
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        #default interface -> the password
        self.SetUI()

        #disabling some default buttons
        self.pushButton_19.setDisabled(True) #UPDATE memeber
        self.pushButton_20.setDisabled(True) #DELETE member
        self.focusOutTable() #UPDATE & DELETE COACH
        self.pushButton_16.setDisabled(True) #ASSIGN coach to a member
        self.pushButton_26.setDisabled(True) #Delete machine button

        #0-Object creation to validate the login data:
        self.validator=validLogin()

        #the Login btn event
        self.pushButton_5.clicked.connect(self.LoginUIvalidation)
        
        #0-Creating Object to handle the members
        self.member=Members()

        #add_member btn event:
        self.pushButton_6.clicked.connect(self.addMemberUI)
         
        #search member event
        self.pushButton_8.clicked.connect(self.SearchMmberUI)

        #clicking on a member event
        self.tableWidget.cellClicked.connect(self.handleClick) #it passes the row and column of the cell
        
        #clicking on "delete" button
        self.current_row = None
        self.pushButton_11.clicked.connect(self.deleteMemberUI)

        #Searching for a specefic user -> show all data
        self.pushButton_12.clicked.connect(self.generalSearch)

        #A-Searching for member to assign:
        self.pushButton_14.clicked.connect(self.searchUserAssignUI)

        #B-Searching for coach to assign
        self.pushButton_15.clicked.connect(self.searchCoachAssignUI)

        #C- global variables:indicate that both member and coach are selected
        self.coachSelected=None
        self.memberSelected=None

        #D-event of selecting a member (cell clicked)
        self.tableWidget_3.cellClicked.connect(self.SelectMemberToAssign)

        #E-event of selecting a coach
        self.tableWidget_4.cellClicked.connect(self.SelectCoachToAssign)

        #F- clicking on assign btn
        self.pushButton_16.clicked.connect(self.assignCoachMemberUI)

        #Object to manage the coachs
        self.Coach=coach()
      
        #Clicking on "Add Coach" btn
        self.pushButton_17.clicked.connect(self.addCoachUI)

        #handling the event of selecting a row from the table
        self.tableWidget_5.cellClicked.connect(self.handleCellCoach)

        #handling search for staff to update/delete
        self.pushButton_18.clicked.connect(self.searchCoachUI)

        #handling the event of clicking on update:
        self.pushButton_19.clicked.connect(self.updateCoachUI1) #slot that:1-switch the tab  2-Set the initial data  3-event for update2

        #handling the event of deleting a coach
        self.currentCoach_row=None
        self.pushButton_20.clicked.connect(self.deleteCoachUI)

        #searching for a coach to show all his data
        self.pushButton_22.clicked.connect(self.generalCoachSearchUI)

        ######Equipements####################
        # Object to handle the equipements
        self.equipement=machine()

        #0-uploading an image
        self.imageBin=None #global variable that stores the binary file of the last uploaded image
        self.pushButton_7.clicked.connect(self.uploadImage)
        #1-ADDING equipement event
        self.pushButton_24.clicked.connect(self.addMachineUI)

        #2-DROPING equipement event
        #A- search for the machine name
        self.pushButton_25.clicked.connect(self.SearchMachine)
        #B-selecting a row from the table
        self.machineSelected=None
        self.tableWidget_7.cellClicked.connect(self.handleSelectMachine)
        #C-clicking on delete
        self.pushButton_26.clicked.connect(self.deleteMachineUI)

        #3-DISPLAY the machine all data
        self.pushButton_27.clicked.connect(self.displayAllMachines)


        #####THE SETTINGS#############
        ##0-object to handle the update
        self.update=validUpdate()
        ##1-update the password
        self.pushButton_29.clicked.connect(self.updatePsswdUI)
        ##2-update the email
        self.pushButton_30.clicked.connect(self.updateMailUI)
             
    #### handling the initial ui ####
    #################################

    def HomePageShowUI(self):
        self.tabWidget.setCurrentIndex(1)
    def MemberManagementUI(self):
        self.tabWidget.setCurrentIndex(2)
    def StaffManagementUI(self):
        self.tabWidget.setCurrentIndex(3)
    def EquipementManagementUI(self):
        self.tabWidget.setCurrentIndex(4)
    def SettingUI(self):
        self.tabWidget.setCurrentIndex(5)
    def hideTabs(self): #hide the tabs
        self.tabWidget.tabBar().hide()
    def defaultUI(self):
        self.tabWidget.setCurrentIndex(0)
    def SetUI(self):
        #1- setting the title
        self.setWindowTitle("GYM Management System")
        #2- setting the default interface
        self.defaultUI()
        self.hideTabs()
        # we disable the buttons until the validation:
        self.InitDisable()
    #method that handles the login:
    def LoginUIvalidation(self):

        #0-connect to the DB:
        self.validator.db.dbConnect()
        #1-get the input text :
        Email=self.lineEdit.text()
        Passwd=self.lineEdit_2.text()
        #2-validating
        if(self.validator.validData(Email,Passwd)):#correct input
            #1-Enable the buttons
            self.LoginEnable()
            #2-show the homePage
            self.HomePageShowUI()
        else:
            QMessageBox.warning(self,"Invalid data","Please ensure correct Admin data before log-in")                  
    #method to disable the buttons:
    def InitDisable(self):
        self.pushButton_3.setDisabled(True)
        self.pushButton_2.setDisabled(True)
        self.pushButton_4.setDisabled(True)
        self.pushButton.setDisabled(True)
        self.pushButton_28.setDisabled(True)
    #method to enable the buttons:
    def LoginEnable(self):
        #1-enable the buttons:
        self.pushButton_3.setDisabled(False)
        self.pushButton_2.setDisabled(False)
        self.pushButton_4.setDisabled(False)
        self.pushButton.setDisabled(False)
        self.pushButton_28.setDisabled(False)

        #2-connect the buttons to the tabs:
        self.pushButton_3.clicked.connect(self.HomePageShowUI)
        self.pushButton_2.clicked.connect(self.MemberManagementUI)
        self.pushButton_4.clicked.connect(self.StaffManagementUI)
        self.pushButton.clicked.connect(self.EquipementManagementUI)
        self.pushButton_28.clicked.connect(self.SettingUI)

#######################################
#######################################    





######### Members management ##########
#######################################    

    def clearAddEdits(self):
        self.lineEdit_3.setText("")
        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_7.setText("")
        self.lineEdit_8.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_9.setText("")

    def clearUpdateEdits(self):
        self.lineEdit_20.setText("")
        self.lineEdit_26.setText("")
        self.lineEdit_25.setText("")
        self.lineEdit_24.setText("")
        self.lineEdit_23.setText("")
        self.lineEdit_22.setText("")
        self.lineEdit_21.setText("")

    
    #1-function called when clicked on ADD member
    def addMemberUI(self):
        
        #0-connect to the db
        self.member.db.dbConnect()
        #1-extract user data
        F_name=self.lineEdit_3.text()
        L_name=self.lineEdit_4.text()
        age=self.lineEdit_5.text()
        gender=self.lineEdit_7.text()
        email=self.lineEdit_8.text()
        phone=self.lineEdit_6.text()
        sessions=self.lineEdit_9.text()
        duration=self.comboBox_6.currentText()

        #1.5-check wether the text is empty
        if(not bool(F_name) or not bool(L_name) or not bool(age) or not bool(gender) or not bool(email) or not bool(phone) or not bool(sessions) or not bool(duration)):
            QMessageBox.warning(self,"Empty column","Please fill all the columns before adding the member")
            return

        #2-add it to the DB
        self.member.addMember(F_name,L_name,age,gender,email,phone,sessions,duration)
        
        #2.5 close the DB connection
        self.member.db.CloseDb()

        #3-clear the lineEdits:
        self.clearAddEdits()

        #declare the addition:
        QMessageBox.information(self,"Insertion completed",f"{F_name} {L_name} is added successfully")

    #used to place the items into the table
    def setTableItems(self,DATA,len):
        self.tableWidget.setRowCount(len) #we created rows to store the fetched data
        for i in range(0,len): #inserting the data into the table
            id= QTableWidgetItem(str(DATA[i][0]))
            self.tableWidget.setItem(i,0,id)

            f_name= QTableWidgetItem(str(DATA[i][1]))
            self.tableWidget.setItem(i,1,f_name)

            l_name= QTableWidgetItem(str(DATA[i][2]))
            self.tableWidget.setItem(i,2,l_name)

            age= QTableWidgetItem(str(DATA[i][3]))
            self.tableWidget.setItem(i,3,age)

            phone=QTableWidgetItem(str(DATA[i][6]))
            self.tableWidget.setItem(i,4,phone)

    #2-function called when Search btn is clicked
    def SearchMmberUI(self):
        #0-connecting to the db
        self.member.db.dbConnect()
        #1-extract the data from the user:
        filter=self.comboBox.currentText()
        data=self.lineEdit_19.text()
        #2-get the data from the DB
        DATA=self.member.searchMember(filter,data)
        #3-close the db
        if(DATA!=None):
            self.member.db.CloseDb()
        #4-place the fetched data into the table
        rowNum=len(DATA)
        self.setTableItems(DATA,rowNum)

    def setForUpdate(self,row:int):
       
        self.lineEdit_20.setText(self.tableWidget.item(row,1).text())
        self.lineEdit_26.setText(self.tableWidget.item(row,2).text())
        self.lineEdit_25.setText(self.tableWidget.item(row,3).text())
        self.lineEdit_22.setText(self.tableWidget.item(row,4).text())
        #2-we get : gender,email,sessions:
        #A- CONNECT TO THE db:
        self.member.db.dbConnect()
        #B-search the information:
        DATA=self.member.searchMember("First Name",self.tableWidget.item(row,1).text())
        #C- closing the DB:
        self.member.db.CloseDb()
        #D- placing the data:
        self.lineEdit_24.setText(str(DATA[row][4]))
        self.lineEdit_23.setText(str(DATA[row][5]))
        self.lineEdit_21.setText(str(DATA[row][8]))
        #E- return the Data:
        return (DATA,row)

    #3-function used to update a member data
    def updateMemberUI1(self,row): #before clicking on update
        #0-we change the tab
        self.MemberTabs.setCurrentIndex(2)

        #0.5-disabling the buttons
        self.focusOutTable()

        #1- we set the initial data on the LineEdits:
        rowData=self.setForUpdate(row)

        #2-we wait for the user to click UPDATE button after modifying
        self.pushButton_10.clicked.connect(lambda:self.updateMemberUI2(rowData))

    def updateMemberUI2(self,rowData:list[tuple]): #eventListener when the user updates data
        #1-extract the data:
        F_name=self.lineEdit_20.text()
        L_name=self.lineEdit_26.text()
        age=self.lineEdit_25.text()
        gender=self.lineEdit_24.text()
        email=self.lineEdit_23.text()
        phone=self.lineEdit_22.text()
        sessions=self.lineEdit_21.text()
        duration=self.comboBox_7.currentText()

        #2-connect to DB:
        self.member.db.dbConnect()
        #3-update:
        DATA,row=rowData[0],rowData[1] #row->the row containing the updated user
        self.member.updateMember(DATA[row][0],F_name,L_name,age,gender,email,phone,sessions,duration)
        #4-close DB:
        self.member.db.commitChange()
        self.member.db.CloseDb()
        #5-clear the Edits:
        self.clearUpdateEdits()


    #function to handle clicking on the table cells
    def handleClick(self,row:int,col):
        print("cell is clicked")
        #0-Enabling the buttons:
        self.pushButton_9.setDisabled(False)
        self.pushButton_11.setDisabled(False)
        #we create eventListener 1 : clicking on update 1 (to move to the next tab)
        self.pushButton_9.clicked.connect(lambda:self.updateMemberUI1(row))

        #updating the clicked row:
        self.current_row=row

    #function to handle focus-out on the table : (disabling update & delete buttons)
    def focusOutTable(self):
        self.pushButton_9.setDisabled(True)
        self.pushButton_11.setDisabled(True)

    def deleteMemberUI(self):
        print(self.current_row)
        if(self.current_row is not None):
            #1-getting the ID :
            if(self.tableWidget.item(self.current_row,0).text()):
                ID=self.tableWidget.item(self.current_row,0).text()
            
            print(ID)
            #2-connect to the db:
            self.member.db.dbConnect()
            #3-delete the member
            print("Before deleting")
            self.member.deleteMember(ID)
            #4-close the db:
            self.member.db.CloseDb()
            #5-reload the search result:
            print("Before filling the table")
            self.SearchMmberUI()
        else:
            print("No row selected")

    #calculate the payment:
    def getPayment(self,duration:str,price:int)->float:
        if(duration=="1 month"):
            return price
        elif(duration=="3 months"):
            return 3*price
        elif(duration=="6 months"):
            return 6*price-((6*price)/10)
        elif(duration=="1 year"):
            return 12*price-((12*price)/20)
        

    #placing values on the large table
    def placeDataLargeTable(self,Data,rowNum):
        print("Placing the data on the table \n\n")
        self.tableWidget_2.setRowCount(rowNum) #we created rows to store the fetched data
        
        for i in range(0,rowNum):
            for j in range(0,7):
                self.tableWidget_2.setItem(i,j,QTableWidgetItem(str(Data[i][j])))
            # sessions perWeek:
            self.tableWidget_2.setItem(i,7,QTableWidgetItem(str(Data[i][8])))
            #the payement: 20$ * duration
            pay=self.getPayment(str(Data[i][10]),20)
            self.tableWidget_2.setItem(i,8,QTableWidgetItem(str(pay)))

        print("Placed the data")                             
    #Searching for all user data
    def generalSearch(self):
        print("generalSearch() is called \n\n")
        #1-extract values and filter
        filter=self.comboBox_2.currentText()
        val=self.lineEdit_27.text()
        
        #2-connect to DB:
        self.member.db.dbConnect()

        #3-search in DB -> return the resulted list
        DATA=self.member.searchMember(filter,val)
        rowNum=len(DATA)
        #4-close the DB
        self.member.db.CloseDb()

        #5-place the data in the table:
        self.placeDataLargeTable(DATA,rowNum)

    def searchUserAssignUI(self):
        #1-extract the data
        filter=self.comboBox_3.currentText()
        val=self.lineEdit_28.text()
        #2-connect to DB:
        self.member.db.dbConnect()
        #3-search for the user:
        DATA=self.member.searchMember(filter,val)
        rowNum=len(DATA)
        #4-close db:
        self.member.db.CloseDb()
        #5-fill the table
        self.fillAssignMemberTable(DATA,rowNum)

    def fillAssignMemberTable(self,DATA,rowNum):
        self.tableWidget_3.setRowCount(rowNum)
        for i in range(0,rowNum):
            self.tableWidget_3.setItem(i,0,QTableWidgetItem(str(DATA[i][0])))
            self.tableWidget_3.setItem(i,1,QTableWidgetItem(str(DATA[i][1])))
            self.tableWidget_3.setItem(i,2,QTableWidgetItem(str(DATA[i][2])))
            self.tableWidget_3.setItem(i,3,QTableWidgetItem(str(DATA[i][3])))
            self.tableWidget_3.setItem(i,4,QTableWidgetItem(str(DATA[i][5])))

    def SelectMemberToAssign(self,row,col):
        self.memberSelected=row #selected member is within ROW:row
        if(self.memberSelected is not None and self.coachSelected is not None):
            self.pushButton_16.setDisabled(False)

    def assignCoachMemberUI(self):
        #1-getting the memberID & coachID from the tables:
        memberID=self.tableWidget_3.item(self.memberSelected,0).text()
        coachID=self.tableWidget_4.item(self.coachSelected,0).text()

        #2-connect to the DB:
        self.member.db.dbConnect()

        #3-update the coach of the member
        assigned=self.member.assignCoach(memberID,coachID)
        
        #4-close db
        self.member.db.CloseDb()

        #5-declare the assignement
        if(assigned):
            QMessageBox.information(self,"Successful coach assignement","Coach is assigned successfully")
        else:
            QMessageBox.warning(self,"Error","Unable to assign coach due to problem,please try again")

##########Staff Management###################
#############################################

    #1- eventListener to adding a coach
    def addCoachUI(self):
        #1-extract data:
        F_name=self.lineEdit_30.text()
        L_name=self.lineEdit_31.text()
        age=self.lineEdit_32.text()
        mail=self.lineEdit_35.text()
        phone=self.lineEdit_33.text()
        dayWeek=self.lineEdit_36.text()
        salary=self.lineEdit_37.text()
        #2-connect to DB
        self.Coach.db.dbConnect()
        #3-add the coach
        added=self.Coach.addCoach(F_name,L_name,age,mail,phone,dayWeek,salary)
        #4-close the DB
        self.Coach.db.CloseDb()
        #5-Clear the edits & declare the addition
        if(added):
            self.clearCoachEdits()
            QMessageBox.information(self,"valid addition",f"{F_name} {L_name} is added succefully")
        else:
            QMessageBox.warning(self,"Failed addition","Unfortunately the coach was not added successfully")

    def clearCoachEdits(self):
        self.lineEdit_30.setText("")
        self.lineEdit_31.setText("")
        self.lineEdit_32.setText("")
        self.lineEdit_35.setText("")
        self.lineEdit_33.setText("")
        self.lineEdit_36.setText("")
        self.lineEdit_37.setText("")

    #2- eventListener to search for coach before update/delete
    def searchCoachUI(self):
        #1-collect the filter and value(data)
        filter=self.comboBox_4.currentText()
        value=self.lineEdit_38.text()
        #2-connect to db:
        self.Coach.db.dbConnect()
        #3-search for the coach:
        DATA=self.Coach.searchCoach(filter,value) #DATA containing the searched rows
        print(DATA)
        if(DATA is not None):
            rowNum=len(DATA)
        #4-close the db:
        self.Coach.db.CloseDb()
        #5-set the data on the table
        self.setDataCoachOnTable(DATA,rowNum)

    def setDataCoachOnTable(self,DATA:list[tuple],rowNum:int):
        #1-create the rows:
        self.tableWidget_5.setRowCount(rowNum)
        #fill the rows
        for i in range(0,rowNum):
            self.tableWidget_5.setItem(i,0,QTableWidgetItem(str(DATA[i][0])))
            self.tableWidget_5.setItem(i,1,QTableWidgetItem(str(DATA[i][1])))
            self.tableWidget_5.setItem(i,2,QTableWidgetItem(str(DATA[i][2])))
            self.tableWidget_5.setItem(i,3,QTableWidgetItem(str(DATA[i][5])))
            self.tableWidget_5.setItem(i,4,QTableWidgetItem(str(DATA[i][6])))
        
    #function that enables the button after selecting the table row (coach)
    def handleCellCoach(self,row:int):
        self.pushButton_19.setDisabled(False)
        self.pushButton_20.setDisabled(False)
        self.currentCoach_row=row #the row of the last clicked coach (selected for update/delete)
    

    def setCoachUpdateData(self,DATA:tuple)->None:
        self.lineEdit_39.setText(str(DATA[1]))
        self.lineEdit_44.setText(str(DATA[2]))
        self.lineEdit_43.setText(str(DATA[3]))
        self.lineEdit_41.setText(str(DATA[4]))
        self.lineEdit_40.setText(str(DATA[5]))
        self.lineEdit_45.setText(str(DATA[6]))
        self.lineEdit_49.setText(str(DATA[7]))
        
    #function when clicking on Update:
    def updateCoachUI1(self,row:int):
        #1-switch to the next tab:
        self.AddMember_2.setCurrentIndex(2)
        #1.5 disable the previous buttons (UPDATE/DELETE)
        self.pushButton_19.setDisabled(True)
        self.pushButton_20.setDisabled(True)
        #2-set the initial data to the edits before editing
            #a-connecting to db
        self.Coach.db.dbConnect()
            #b-get data
        DATA=self.Coach.searchCoach("First Name",self.lineEdit_38.text())
        clickedRow=DATA[row]
            #c-close the db:
        self.Coach.db.CloseDb()
        #3-now we put the data on the lineEdits:
        self.setCoachUpdateData(clickedRow)
        #4-waiting for the "update btn" event
        id=clickedRow[0]
        self.pushButton_21.clicked.connect(lambda:self.updateCoachUI2(id)) #it takes the id of the user to update

    #function that handles the update of coach data

     #A- to extract updated coach data
    def extractUpdatedCoachData(self):
        F_name=self.lineEdit_39.text()
        L_name=self.lineEdit_44.text()
        age=self.lineEdit_43.text()
        email=self.lineEdit_41.text()
        phone=self.lineEdit_40.text()
        dayWeek=self.lineEdit_45.text()
        salary=self.lineEdit_49.text()
        return (F_name,L_name,age,email,phone,dayWeek,salary)

     #B-to clear the Edits after successful update    
    
    def clearUpdateEdits(self):
        self.lineEdit_39.setText("")
        self.lineEdit_44.setText("")
        self.lineEdit_43.setText("")
        self.lineEdit_41.setText("")
        self.lineEdit_40.setText("")
        self.lineEdit_45.setText("")
        self.lineEdit_49.setText("")
 
     #--> MAIN FUNCTION
    
    def updateCoachUI2(self,id:str):
        #1-extract the data:
        updatedData=self.extractUpdatedCoachData()
        #2-connect to the DB
        self.Coach.db.dbConnect()
        #3-update the coach data
        updated=self.Coach.updateCoach(id,updatedData)
        #4-clear the edits and declare the update
        if(updated):
            self.clearUpdateEdits()
            QMessageBox.information(self,"Successful update","User updated successfully")

    #function to delete a selected coach
    def deleteCoachUI(self):
        #1-we get the id
        id=self.tableWidget_5.item(self.currentCoach_row,0).text()
        #2-connect to the db:
        self.Coach.db.dbConnect()
        #delete the user
        self.Coach.deleteCoach(id)
        #close the db:
        self.Coach.db.CloseDb()
        #reload the data base to fill the table
        self.searchCoachUI()

    #function that display all the search coach data
    def generalCoachSearchUI(self):
        print("extract filter & value")
        #1-extract filter & value
        filter=self.comboBox_5.currentText()
        Value=self.lineEdit_46.text()
        #2-connect to DB
        self.Coach.db.dbConnect()
        #3-fetch data from db
        DATA=self.Coach.searchCoach(filter,Value)
        length=len(DATA)
        print(DATA)
        #4-close dataBase
        self.Coach.db.CloseDb()
        #5-set the data into the table
        self.setCoachAlldataToTable(DATA,length)

    #function to fill the general table
    def setCoachAlldataToTable(self,DATA:list[tuple],length:int): #set data on table & return id to use it after
        #1-create the rows
        self.tableWidget_6.setRowCount(length)
        print(f"{length} rows created")
        #1.5-connect to DB:
        self.Coach.db.dbConnect()
        #2-fill the table
        for i in range(0,length):
            for j in range(0,8):
                self.tableWidget_6.setItem(i,j,QTableWidgetItem(str(DATA[i][j])))
            # we set the trainees of each row ->we use searchTrainees :
            rowTrainees=self.Coach.searchTrainees(str(DATA[i][0])) #-> the id column of each coach row
            #then we place them on the table row    
            self.tableWidget_6.setItem(i,8,QTableWidgetItem(str(rowTrainees)))

            #######Do it later : function to format the output before adding it to the table

        self.Coach.db.CloseDb()
   
    #search for coach to assign:
    def searchCoachAssignUI(self):
        #1-extract data
        filter=self.comboBox_8.currentText()
        val=self.lineEdit_29.text()
        #DB connection
        self.Coach.db.dbConnect()
        #Search for coach
        DATA=self.Coach.searchCoach(filter,val)
        rowNum=len(DATA)
        #close DB
        self.Coach.db.CloseDb()
        #insert into the table
        self.setTableCoachAssign(DATA,rowNum)

    def setTableCoachAssign(self,DATA,rowNum):
        self.tableWidget_4.setRowCount(rowNum)
        for i in range(0,rowNum):
            self.tableWidget_4.setItem(i,0,QTableWidgetItem(str(DATA[i][0])))
            self.tableWidget_4.setItem(i,1,QTableWidgetItem(str(DATA[i][1])))
            self.tableWidget_4.setItem(i,2,QTableWidgetItem(str(DATA[i][2])))
            self.tableWidget_4.setItem(i,3,QTableWidgetItem(str(DATA[i][5])))
            self.tableWidget_4.setItem(i,4,QTableWidgetItem(str(DATA[i][6])))

    def SelectCoachToAssign(self,row,col):
        self.coachSelected=row
        if(self.coachSelected is not None and self.memberSelected is not None): #enable the btn
            self.pushButton_16.setDisabled(False)

    #######################################
    #######################################    





    ######### Equipements management###########
    ###########################################

    #0-event of uploading an image
    def uploadImage(self):
        #1- select the image from the file system
        imagePath,_=QFileDialog.getOpenFileName(self,caption="Select Image",filter="Images (*.png *.jpg *.bmp *)")
        #2-convert it into binary data to store it in self.imageBin variable
        if(imagePath):
            with open(imagePath, 'rb') as file: #1-open the image in binary mode "b"  
                                                #2-return object "file"representing the binary file  
                self.imageBin = file.read() #3-read the binary data and store the content 
 
    #1-event of adding a machine
    def addMachineUI(self):
        #1-extract data
        machineName=self.lineEdit_48.text()
        cost=self.lineEdit_47.text()
        description=self.textEdit.toPlainText()
        imgBin=self.imageBin
        #2-connect to DB
        self.equipement.db.dbConnect()
        #3-store the data:
        stored=self.equipement.storeMachineData(machineName,cost,description,imgBin)
        #3-declare the add
        if(stored):
            self.clearMachineAdd()
            QMessageBox.information(self,"Machine added",f"{machineName} is added successfully")

    def clearMachineAdd(self):
        self.lineEdit_48.setText("")
        self.lineEdit_47.setText("")
        self.textEdit.setText("")

    def SearchMachine(self):
        #1-extract data:
        machineName=self.lineEdit_51.text()
        print(machineName)
        #2-connect to DB
        self.equipement.db.dbConnect()
        #3-search for the machines
        DATA=self.equipement.searchMachine(machineName)
        rowNum=len(DATA)
        print(DATA)
        #4- FILL THE TABLE WITH DATA
        self.setMachinesAtTable(DATA,rowNum)

    def setMachinesAtTable(self,DATA,rowNum):
        self.tableWidget_7.setRowCount(rowNum)
        print(f"{rowNum} row created")
        for i in range(0,rowNum):
            for j in range(0,5):
                self.tableWidget_7.setItem(i,j,QTableWidgetItem(str(DATA[i][j])))

    #2- event of selecting a machine from table
    def handleSelectMachine(self,row:int,col:int)->None:
        #1-enable delete button 
        self.pushButton_26.setDisabled(False)
        #2-store the selected machine
        self.machineSelected=row  #the row of the table (int)

    #3- event of droping a machine
    def deleteMachineUI(self):
        #1-we get the id
        id=self.tableWidget_7.item(self.machineSelected,0).text() 
        #2-connect to the db:
        self.equipement.db.dbConnect()
        #delete the user
        deleted=self.equipement.deleteMachine(id)
        #close the db:
        self.equipement.db.CloseDb()
        #reload the data base to fill the table
        self.SearchMachine()
        #declare the deletion
        if(deleted):
            QMessageBox.warning(self,"Successful deletion","Machine is deleted successfully")
     
    #4-event of searching to display all machine data
    def displayAllMachines(self):
        #1-extract the name
        machineName=self.lineEdit_52.text()
        #2-connect to the Db
        self.equipement.db.dbConnect()
        #3-search for machines
        DATA=self.equipement.searchMachine(machineName)
        rows=len(DATA)
        #4-close DB
        self.equipement.db.CloseDb()
        #5-display the data
        self.setAllMachineData(DATA,rows)


    def setAllMachineData(self,DATA:list[tuple],rows:int)->None:
        self.tableWidget_8.setRowCount(rows)
        for i in range(0,rows):
            for j in range(0,5):
                self.tableWidget_8.setItem(i,j,QTableWidgetItem(str(DATA[i][j])))
            #B-we display the image
            imageBin = DATA[i][5]
            imageBin = base64.b64decode(imageBin)
            print(imageBin)
            if imageBin:
                print("image binaries was loaded")
                pixmap = QPixmap()
                pixmap.loadFromData(imageBin)
                print(pixmap)
                if not pixmap.isNull():
                    print("image is converted into pixmap")
                    pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                
                    # Create a QLabel and set the pixmap
                    label = QLabel()
                    label.setPixmap(pixmap) #Union[PySide6.QtGui.QPixmap, PySide6.QtGui.QImage
                    label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                    # Set the label as the cell widget
                    self.tableWidget_8.setCellWidget(i, 5, label)
                
                    # Adjust row height
                    self.tableWidget_8.setRowHeight(i, 100)
                else:
                    print(f"failed to load the image for row {i}")
                    self.tableWidget_8.setItem(i, 5, QTableWidgetItem("Failed to load image"))
            else: 
                self.tableWidget_8.setItem(i, 5, QTableWidgetItem("No image available"))
    
        # Force update
        self.tableWidget_8.viewport().update()



##########SETTINGS#################
###################################

#event of updating the password
    def updatePsswdUI(self):
        #1-extract data
        currPsswd=self.lineEdit_55.text()
        newPsswd=self.lineEdit_53.text()
        confirm=self.lineEdit_54.text()
        #2-check confirmation
        if(newPsswd!=confirm):
            QMessageBox.warning(self,"Error","The new password is not similar to its confirmation")
        #3-connect to db
        self.update.db.dbConnect()
        #4-update the password
        result=self.update.updatePassword(currPsswd,newPsswd)
        #5-close the db
        self.update.db.CloseDb()
        #6-declare the update
        if(result[0]):
            QMessageBox.information(self,"Updated","Password is updated successfully")
            self.lineEdit_55.setText("")
            self.lineEdit_53.setText("")
            self.lineEdit_54.setText("")
        else: #not updated
            QMessageBox.warning(self,"",result[1])

    def updateMailUI(self):
        #1-extract data
        currMail=self.lineEdit_57.text()
        newMail=self.lineEdit_56.text()
        #2-connect to db
        self.update.db.dbConnect()
        #3-update the email
        result=self.update.updateEmail(currMail,newMail)
        #5-close the db
        self.update.db.CloseDb()
        #6-declare the update
        if(result[0]):
            QMessageBox.information(self,"Updated","Email is updated successfully")
            self.lineEdit_57.setText("")
            self.lineEdit_56.setText("")
        else: #not updated
            QMessageBox.warning(self,"",result[1])



if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainPage()
    widget.show()
    sys.exit(app.exec())
