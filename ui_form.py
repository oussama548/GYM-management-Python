# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QTabWidget, QTableWidget, QTableWidgetItem, QTextEdit,
    QVBoxLayout, QWidget)
import rc_icons

class Ui_MainPage(object):
    def setupUi(self, MainPage):
        if not MainPage.objectName():
            MainPage.setObjectName(u"MainPage")
        MainPage.resize(1479, 711)
        icon = QIcon()
        icon.addFile(u"icons/salle.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainPage.setWindowIcon(icon)
        MainPage.setStyleSheet(u"")
        MainPage.setIconSize(QSize(45, 45))
        self.centralwidget = QWidget(MainPage)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(280, 0, 1191, 681))
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label = QLabel(self.tab)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 1191, 631))
        self.label.setStyleSheet(u"background-image: url(:/icon/images/bg.jpg);\n"
"background-repeat:no-repeat;")
        self.label.setPixmap(QPixmap(u":/icon/images/bg.jpg"))
        self.label.setScaledContents(True)
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(200, 130, 741, 361))
        self.widget.setStyleSheet(u"background-color: rgb(167, 167, 167);\n"
"border-radius:15px;")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 50, 511, 61))
        self.lineEdit.setStyleSheet(u"border:1px solid black;\n"
"border-radius:5px;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"color:black;\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size:12pt;")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(120, 130, 511, 61))
        self.lineEdit_2.setStyleSheet(u"border:1px solid black;\n"
"border-radius:5px;\n"
"padding-right:10px;\n"
"padding-left:10px;\n"
"color:black;\n"
"font: 700 9pt \"Segoe UI\";\n"
"font-size:12pt;")
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(280, 240, 171, 71))
        self.pushButton_5.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_5.setStyleSheet(u"border:1px solid black;\n"
"border-radius:10px;\n"
"color:black;\n"
"background-color: rgb(217, 217, 217);\n"
"font: 700 16pt \"Segoe UI\";")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.label_2 = QLabel(self.tab_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 1191, 631))
        self.label_2.setStyleSheet(u"background-image: url(:/icon/images/bg.jpg);\n"
"background-repeat:no-repeat;")
        self.label_2.setPixmap(QPixmap(u":/icon/images/bg.jpg"))
        self.label_2.setScaledContents(True)
        self.label_61 = QLabel(self.tab_2)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(150, 40, 881, 141))
        self.label_61.setStyleSheet(u"color:rgb(0, 0, 0);\n"
"background-color: rgb(179, 179, 179);\n"
"font: 700 22pt \"Segoe UI\";\n"
"border-radius:60px;\n"
"text-align:center;")
        self.label_61.setAlignment(Qt.AlignCenter)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.MemberTabs = QTabWidget(self.tab_7)
        self.MemberTabs.setObjectName(u"MemberTabs")
        self.MemberTabs.setGeometry(QRect(0, 0, 1191, 631))
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.horizontalLayoutWidget = QWidget(self.tab_6)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 30, 511, 51))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.label_3)

        self.lineEdit_3 = QLineEdit(self.horizontalLayoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.lineEdit_3)

        self.horizontalLayoutWidget_2 = QWidget(self.tab_6)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(20, 100, 511, 51))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 600 12pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.lineEdit_4 = QLineEdit(self.horizontalLayoutWidget_2)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_2.addWidget(self.lineEdit_4)

        self.horizontalLayoutWidget_3 = QWidget(self.tab_6)
        self.horizontalLayoutWidget_3.setObjectName(u"horizontalLayoutWidget_3")
        self.horizontalLayoutWidget_3.setGeometry(QRect(20, 180, 511, 51))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.horizontalLayoutWidget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.lineEdit_5 = QLineEdit(self.horizontalLayoutWidget_3)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(False)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_3.addWidget(self.lineEdit_5)

        self.horizontalLayoutWidget_4 = QWidget(self.tab_6)
        self.horizontalLayoutWidget_4.setObjectName(u"horizontalLayoutWidget_4")
        self.horizontalLayoutWidget_4.setGeometry(QRect(20, 420, 511, 51))
        self.horizontalLayout_4 = QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.horizontalLayoutWidget_4)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 600 12pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_4.addWidget(self.label_6)

        self.lineEdit_6 = QLineEdit(self.horizontalLayoutWidget_4)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_4.addWidget(self.lineEdit_6)

        self.horizontalLayoutWidget_5 = QWidget(self.tab_6)
        self.horizontalLayoutWidget_5.setObjectName(u"horizontalLayoutWidget_5")
        self.horizontalLayoutWidget_5.setGeometry(QRect(20, 260, 511, 51))
        self.horizontalLayout_5 = QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.horizontalLayoutWidget_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_5.addWidget(self.label_7)

        self.lineEdit_7 = QLineEdit(self.horizontalLayoutWidget_5)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_5.addWidget(self.lineEdit_7)

        self.horizontalLayoutWidget_6 = QWidget(self.tab_6)
        self.horizontalLayoutWidget_6.setObjectName(u"horizontalLayoutWidget_6")
        self.horizontalLayoutWidget_6.setGeometry(QRect(20, 340, 511, 51))
        self.horizontalLayout_6 = QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.horizontalLayoutWidget_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.label_8)

        self.lineEdit_8 = QLineEdit(self.horizontalLayoutWidget_6)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        self.lineEdit_8.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_6.addWidget(self.lineEdit_8)

        self.horizontalLayoutWidget_7 = QWidget(self.tab_6)
        self.horizontalLayoutWidget_7.setObjectName(u"horizontalLayoutWidget_7")
        self.horizontalLayoutWidget_7.setGeometry(QRect(610, 90, 511, 51))
        self.horizontalLayout_8 = QHBoxLayout(self.horizontalLayoutWidget_7)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_9 = QLabel(self.horizontalLayoutWidget_7)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.label_9)

        self.lineEdit_9 = QLineEdit(self.horizontalLayoutWidget_7)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        self.lineEdit_9.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_8.addWidget(self.lineEdit_9)

        self.horizontalLayoutWidget_9 = QWidget(self.tab_6)
        self.horizontalLayoutWidget_9.setObjectName(u"horizontalLayoutWidget_9")
        self.horizontalLayoutWidget_9.setGeometry(QRect(610, 160, 251, 51))
        self.horizontalLayout_10 = QHBoxLayout(self.horizontalLayoutWidget_9)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.horizontalLayoutWidget_9)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_10.addWidget(self.label_11)

        self.comboBox_6 = QComboBox(self.horizontalLayoutWidget_9)
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.setObjectName(u"comboBox_6")
        self.comboBox_6.setStyleSheet(u"height:35px;\n"
"font: 350 11pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_10.addWidget(self.comboBox_6)

        self.pushButton_6 = QPushButton(self.tab_6)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(680, 300, 291, 91))
        self.pushButton_6.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_6.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.MemberTabs.addTab(self.tab_6, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName(u"tab_8")
        self.label_19 = QLabel(self.tab_8)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(40, 10, 291, 41))
        self.label_19.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.horizontalLayoutWidget_17 = QWidget(self.tab_8)
        self.horizontalLayoutWidget_17.setObjectName(u"horizontalLayoutWidget_17")
        self.horizontalLayoutWidget_17.setGeometry(QRect(40, 50, 1041, 80))
        self.horizontalLayout_18 = QHBoxLayout(self.horizontalLayoutWidget_17)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.label_20 = QLabel(self.horizontalLayoutWidget_17)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setStyleSheet(u"font: 600 14pt \"Segoe UI\";")

        self.horizontalLayout_18.addWidget(self.label_20)

        self.comboBox = QComboBox(self.horizontalLayoutWidget_17)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"width:120px;\n"
"margin-right:50px;\n"
"margin-left:50px;\n"
"height:40px;\n"
"padding-left:7px;")

        self.horizontalLayout_18.addWidget(self.comboBox)

        self.lineEdit_19 = QLineEdit(self.horizontalLayoutWidget_17)
        self.lineEdit_19.setObjectName(u"lineEdit_19")
        self.lineEdit_19.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"margin-right:80px;")

        self.horizontalLayout_18.addWidget(self.lineEdit_19)

        self.pushButton_8 = QPushButton(self.horizontalLayoutWidget_17)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_8.setStyleSheet(u"margin-right:15px;\n"
"width:100px;\n"
"font: 600 14pt \"Segoe UI\";\n"
"heigth:60px;")

        self.horizontalLayout_18.addWidget(self.pushButton_8)

        self.tableWidget = QTableWidget(self.tab_8)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 150, 911, 431))
        self.tableWidget.setStyleSheet(u"border:0.5px solid white;\n"
"color:white;\n"
"background-color: rgb(117, 117, 117);\n"
"font-size:12pt;\n"
"font-weigth:600;")
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.pushButton_9 = QPushButton(self.tab_8)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(970, 220, 181, 91))
        self.pushButton_9.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_9.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.pushButton_11 = QPushButton(self.tab_8)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(970, 400, 181, 91))
        self.pushButton_11.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_11.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.MemberTabs.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName(u"tab_9")
        self.horizontalLayoutWidget_18 = QWidget(self.tab_9)
        self.horizontalLayoutWidget_18.setObjectName(u"horizontalLayoutWidget_18")
        self.horizontalLayoutWidget_18.setGeometry(QRect(30, 20, 411, 61))
        self.horizontalLayout_19 = QHBoxLayout(self.horizontalLayoutWidget_18)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.horizontalLayoutWidget_18)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_19.addWidget(self.label_21)

        self.lineEdit_20 = QLineEdit(self.horizontalLayoutWidget_18)
        self.lineEdit_20.setObjectName(u"lineEdit_20")
        self.lineEdit_20.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_19.addWidget(self.lineEdit_20)

        self.horizontalLayoutWidget_20 = QWidget(self.tab_9)
        self.horizontalLayoutWidget_20.setObjectName(u"horizontalLayoutWidget_20")
        self.horizontalLayoutWidget_20.setGeometry(QRect(30, 420, 411, 61))
        self.horizontalLayout_21 = QHBoxLayout(self.horizontalLayoutWidget_20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_23 = QLabel(self.horizontalLayoutWidget_20)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_21.addWidget(self.label_23)

        self.lineEdit_22 = QLineEdit(self.horizontalLayoutWidget_20)
        self.lineEdit_22.setObjectName(u"lineEdit_22")
        self.lineEdit_22.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_21.addWidget(self.lineEdit_22)

        self.horizontalLayoutWidget_21 = QWidget(self.tab_9)
        self.horizontalLayoutWidget_21.setObjectName(u"horizontalLayoutWidget_21")
        self.horizontalLayoutWidget_21.setGeometry(QRect(30, 340, 411, 61))
        self.horizontalLayout_22 = QHBoxLayout(self.horizontalLayoutWidget_21)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.label_24 = QLabel(self.horizontalLayoutWidget_21)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.label_24)

        self.lineEdit_23 = QLineEdit(self.horizontalLayoutWidget_21)
        self.lineEdit_23.setObjectName(u"lineEdit_23")
        self.lineEdit_23.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_22.addWidget(self.lineEdit_23)

        self.horizontalLayoutWidget_22 = QWidget(self.tab_9)
        self.horizontalLayoutWidget_22.setObjectName(u"horizontalLayoutWidget_22")
        self.horizontalLayoutWidget_22.setGeometry(QRect(30, 260, 411, 61))
        self.horizontalLayout_23 = QHBoxLayout(self.horizontalLayoutWidget_22)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_25 = QLabel(self.horizontalLayoutWidget_22)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 600 12pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_23.addWidget(self.label_25)

        self.lineEdit_24 = QLineEdit(self.horizontalLayoutWidget_22)
        self.lineEdit_24.setObjectName(u"lineEdit_24")
        self.lineEdit_24.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_23.addWidget(self.lineEdit_24)

        self.horizontalLayoutWidget_23 = QWidget(self.tab_9)
        self.horizontalLayoutWidget_23.setObjectName(u"horizontalLayoutWidget_23")
        self.horizontalLayoutWidget_23.setGeometry(QRect(30, 180, 411, 61))
        self.horizontalLayout_24 = QHBoxLayout(self.horizontalLayoutWidget_23)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.horizontalLayoutWidget_23)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_24.addWidget(self.label_26)

        self.lineEdit_25 = QLineEdit(self.horizontalLayoutWidget_23)
        self.lineEdit_25.setObjectName(u"lineEdit_25")
        self.lineEdit_25.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_24.addWidget(self.lineEdit_25)

        self.horizontalLayoutWidget_24 = QWidget(self.tab_9)
        self.horizontalLayoutWidget_24.setObjectName(u"horizontalLayoutWidget_24")
        self.horizontalLayoutWidget_24.setGeometry(QRect(30, 100, 411, 61))
        self.horizontalLayout_25 = QHBoxLayout(self.horizontalLayoutWidget_24)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_27 = QLabel(self.horizontalLayoutWidget_24)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_25.addWidget(self.label_27)

        self.lineEdit_26 = QLineEdit(self.horizontalLayoutWidget_24)
        self.lineEdit_26.setObjectName(u"lineEdit_26")
        self.lineEdit_26.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_25.addWidget(self.lineEdit_26)

        self.label_22 = QLabel(self.tab_9)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(660, 10, 321, 71))
        self.horizontalLayoutWidget_19 = QWidget(self.tab_9)
        self.horizontalLayoutWidget_19.setObjectName(u"horizontalLayoutWidget_19")
        self.horizontalLayoutWidget_19.setGeometry(QRect(590, 90, 421, 61))
        self.horizontalLayout_20 = QHBoxLayout(self.horizontalLayoutWidget_19)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.label_28 = QLabel(self.horizontalLayoutWidget_19)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_20.addWidget(self.label_28)

        self.lineEdit_21 = QLineEdit(self.horizontalLayoutWidget_19)
        self.lineEdit_21.setObjectName(u"lineEdit_21")
        self.lineEdit_21.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_20.addWidget(self.lineEdit_21)

        self.pushButton_10 = QPushButton(self.tab_9)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(690, 310, 291, 101))
        self.pushButton_10.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_10.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.horizontalLayoutWidget_10 = QWidget(self.tab_9)
        self.horizontalLayoutWidget_10.setObjectName(u"horizontalLayoutWidget_10")
        self.horizontalLayoutWidget_10.setGeometry(QRect(590, 190, 251, 51))
        self.horizontalLayout_11 = QHBoxLayout(self.horizontalLayoutWidget_10)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.horizontalLayoutWidget_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_11.addWidget(self.label_12)

        self.comboBox_7 = QComboBox(self.horizontalLayoutWidget_10)
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.setObjectName(u"comboBox_7")
        self.comboBox_7.setStyleSheet(u"height:35px;\n"
"font: 350 11pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_11.addWidget(self.comboBox_7)

        self.MemberTabs.addTab(self.tab_9, "")
        self.tab_10 = QWidget()
        self.tab_10.setObjectName(u"tab_10")
        self.horizontalLayoutWidget_26 = QWidget(self.tab_10)
        self.horizontalLayoutWidget_26.setObjectName(u"horizontalLayoutWidget_26")
        self.horizontalLayoutWidget_26.setGeometry(QRect(60, 20, 1041, 80))
        self.horizontalLayout_27 = QHBoxLayout(self.horizontalLayoutWidget_26)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.label_31 = QLabel(self.horizontalLayoutWidget_26)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setStyleSheet(u"font: 600 14pt \"Segoe UI\";")

        self.horizontalLayout_27.addWidget(self.label_31)

        self.comboBox_2 = QComboBox(self.horizontalLayoutWidget_26)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"margin-right:50px;\n"
"margin-left:50px;\n"
"height:40px;\n"
"width:120px;\n"
"padding-left:7px;")

        self.horizontalLayout_27.addWidget(self.comboBox_2)

        self.lineEdit_27 = QLineEdit(self.horizontalLayoutWidget_26)
        self.lineEdit_27.setObjectName(u"lineEdit_27")
        self.lineEdit_27.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"margin-right:80px;")

        self.horizontalLayout_27.addWidget(self.lineEdit_27)

        self.pushButton_12 = QPushButton(self.horizontalLayoutWidget_26)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_12.setStyleSheet(u"margin-right:15px;\n"
"width:100px;\n"
"font: 600 14pt \"Segoe UI\";\n"
"heigth:60px;")

        self.horizontalLayout_27.addWidget(self.pushButton_12)

        self.tableWidget_2 = QTableWidget(self.tab_10)
        if (self.tableWidget_2.columnCount() < 9):
            self.tableWidget_2.setColumnCount(9)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font2);
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem13)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(0, 100, 1181, 451))
        self.tableWidget_2.setStyleSheet(u"border:0.5px solid white;\n"
"color:white;\n"
"background-color: rgb(117, 117, 117);\n"
"font-size:12pt;\n"
"font-weigth:600;")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(131)
        self.MemberTabs.addTab(self.tab_10, "")
        self.tab_17 = QWidget()
        self.tab_17.setObjectName(u"tab_17")
        self.horizontalLayoutWidget_27 = QWidget(self.tab_17)
        self.horizontalLayoutWidget_27.setObjectName(u"horizontalLayoutWidget_27")
        self.horizontalLayoutWidget_27.setGeometry(QRect(0, 10, 581, 80))
        self.horizontalLayout_28 = QHBoxLayout(self.horizontalLayoutWidget_27)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.horizontalLayoutWidget_27)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 600 11pt \"Segoe UI\";")

        self.horizontalLayout_28.addWidget(self.label_32)

        self.comboBox_3 = QComboBox(self.horizontalLayoutWidget_27)
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setObjectName(u"comboBox_3")
        self.comboBox_3.setStyleSheet(u"width:120px;\n"
"height:40px;\n"
"padding-left:7px;")

        self.horizontalLayout_28.addWidget(self.comboBox_3)

        self.lineEdit_28 = QLineEdit(self.horizontalLayoutWidget_27)
        self.lineEdit_28.setObjectName(u"lineEdit_28")
        self.lineEdit_28.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"width:60px;\n"
"")

        self.horizontalLayout_28.addWidget(self.lineEdit_28)

        self.pushButton_14 = QPushButton(self.horizontalLayoutWidget_27)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_14.setStyleSheet(u"margin-right:15px;\n"
"width:100px;\n"
"font: 600 14pt \"Segoe UI\";\n"
"heigth:60px;")

        self.horizontalLayout_28.addWidget(self.pushButton_14)

        self.tableWidget_3 = QTableWidget(self.tab_17)
        if (self.tableWidget_3.columnCount() < 6):
            self.tableWidget_3.setColumnCount(6)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(10, 100, 571, 361))
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(100)
        self.horizontalLayoutWidget_28 = QWidget(self.tab_17)
        self.horizontalLayoutWidget_28.setObjectName(u"horizontalLayoutWidget_28")
        self.horizontalLayoutWidget_28.setGeometry(QRect(610, 10, 571, 80))
        self.horizontalLayout_29 = QHBoxLayout(self.horizontalLayoutWidget_28)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_33 = QLabel(self.horizontalLayoutWidget_28)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 600 11pt \"Segoe UI\";")

        self.horizontalLayout_29.addWidget(self.label_33)

        self.comboBox_8 = QComboBox(self.horizontalLayoutWidget_28)
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.setObjectName(u"comboBox_8")
        self.comboBox_8.setStyleSheet(u"width:120px;\n"
"height:40px;\n"
"padding-left:7px;")

        self.horizontalLayout_29.addWidget(self.comboBox_8)

        self.lineEdit_29 = QLineEdit(self.horizontalLayoutWidget_28)
        self.lineEdit_29.setObjectName(u"lineEdit_29")
        self.lineEdit_29.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"width:60px;\n"
"")

        self.horizontalLayout_29.addWidget(self.lineEdit_29)

        self.pushButton_15 = QPushButton(self.horizontalLayoutWidget_28)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_15.setStyleSheet(u"margin-right:15px;\n"
"width:100px;\n"
"font: 600 14pt \"Segoe UI\";\n"
"heigth:60px;")

        self.horizontalLayout_29.addWidget(self.pushButton_15)

        self.tableWidget_4 = QTableWidget(self.tab_17)
        if (self.tableWidget_4.columnCount() < 5):
            self.tableWidget_4.setColumnCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(610, 100, 571, 361))
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(110)
        self.pushButton_16 = QPushButton(self.tab_17)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(440, 480, 291, 91))
        self.pushButton_16.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_16.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.line = QFrame(self.tab_17)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(580, 20, 20, 431))
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.MemberTabs.addTab(self.tab_17, "")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName(u"tab_3")
        self.AddMember_2 = QTabWidget(self.tab_3)
        self.AddMember_2.setObjectName(u"AddMember_2")
        self.AddMember_2.setGeometry(QRect(0, 0, 1191, 631))
        self.tab_15 = QWidget()
        self.tab_15.setObjectName(u"tab_15")
        self.horizontalLayoutWidget_29 = QWidget(self.tab_15)
        self.horizontalLayoutWidget_29.setObjectName(u"horizontalLayoutWidget_29")
        self.horizontalLayoutWidget_29.setGeometry(QRect(20, 30, 511, 51))
        self.horizontalLayout_30 = QHBoxLayout(self.horizontalLayoutWidget_29)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_34 = QLabel(self.horizontalLayoutWidget_29)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_30.addWidget(self.label_34)

        self.lineEdit_30 = QLineEdit(self.horizontalLayoutWidget_29)
        self.lineEdit_30.setObjectName(u"lineEdit_30")
        self.lineEdit_30.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_30.addWidget(self.lineEdit_30)

        self.horizontalLayoutWidget_30 = QWidget(self.tab_15)
        self.horizontalLayoutWidget_30.setObjectName(u"horizontalLayoutWidget_30")
        self.horizontalLayoutWidget_30.setGeometry(QRect(20, 100, 511, 51))
        self.horizontalLayout_31 = QHBoxLayout(self.horizontalLayoutWidget_30)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.horizontalLayoutWidget_30)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 600 12pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_31.addWidget(self.label_35)

        self.lineEdit_31 = QLineEdit(self.horizontalLayoutWidget_30)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_31.addWidget(self.lineEdit_31)

        self.horizontalLayoutWidget_31 = QWidget(self.tab_15)
        self.horizontalLayoutWidget_31.setObjectName(u"horizontalLayoutWidget_31")
        self.horizontalLayoutWidget_31.setGeometry(QRect(20, 180, 511, 51))
        self.horizontalLayout_32 = QHBoxLayout(self.horizontalLayoutWidget_31)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.label_36 = QLabel(self.horizontalLayoutWidget_31)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_32.addWidget(self.label_36)

        self.lineEdit_32 = QLineEdit(self.horizontalLayoutWidget_31)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_32.addWidget(self.lineEdit_32)

        self.horizontalLayoutWidget_32 = QWidget(self.tab_15)
        self.horizontalLayoutWidget_32.setObjectName(u"horizontalLayoutWidget_32")
        self.horizontalLayoutWidget_32.setGeometry(QRect(20, 340, 511, 51))
        self.horizontalLayout_33 = QHBoxLayout(self.horizontalLayoutWidget_32)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.label_37 = QLabel(self.horizontalLayoutWidget_32)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 600 12pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_33.addWidget(self.label_37)

        self.lineEdit_33 = QLineEdit(self.horizontalLayoutWidget_32)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"")

        self.horizontalLayout_33.addWidget(self.lineEdit_33)

        self.horizontalLayoutWidget_34 = QWidget(self.tab_15)
        self.horizontalLayoutWidget_34.setObjectName(u"horizontalLayoutWidget_34")
        self.horizontalLayoutWidget_34.setGeometry(QRect(20, 260, 511, 51))
        self.horizontalLayout_35 = QHBoxLayout(self.horizontalLayoutWidget_34)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.label_39 = QLabel(self.horizontalLayoutWidget_34)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_35.addWidget(self.label_39)

        self.lineEdit_35 = QLineEdit(self.horizontalLayoutWidget_34)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_35.addWidget(self.lineEdit_35)

        self.horizontalLayoutWidget_35 = QWidget(self.tab_15)
        self.horizontalLayoutWidget_35.setObjectName(u"horizontalLayoutWidget_35")
        self.horizontalLayoutWidget_35.setGeometry(QRect(20, 420, 511, 51))
        self.horizontalLayout_36 = QHBoxLayout(self.horizontalLayoutWidget_35)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.horizontalLayoutWidget_35)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_36.addWidget(self.label_40)

        self.lineEdit_36 = QLineEdit(self.horizontalLayoutWidget_35)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_36.addWidget(self.lineEdit_36)

        self.horizontalLayoutWidget_36 = QWidget(self.tab_15)
        self.horizontalLayoutWidget_36.setObjectName(u"horizontalLayoutWidget_36")
        self.horizontalLayoutWidget_36.setGeometry(QRect(610, 160, 511, 51))
        self.horizontalLayout_37 = QHBoxLayout(self.horizontalLayoutWidget_36)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_37.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.horizontalLayoutWidget_36)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_37.addWidget(self.label_41)

        self.lineEdit_37 = QLineEdit(self.horizontalLayoutWidget_36)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_37.addWidget(self.lineEdit_37)

        self.pushButton_17 = QPushButton(self.tab_15)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(680, 300, 291, 91))
        self.pushButton_17.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_17.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.AddMember_2.addTab(self.tab_15, "")
        self.tab_16 = QWidget()
        self.tab_16.setObjectName(u"tab_16")
        self.label_42 = QLabel(self.tab_16)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setGeometry(QRect(40, 10, 291, 41))
        self.label_42.setStyleSheet(u"font: 700 16pt \"Segoe UI\";")
        self.horizontalLayoutWidget_37 = QWidget(self.tab_16)
        self.horizontalLayoutWidget_37.setObjectName(u"horizontalLayoutWidget_37")
        self.horizontalLayoutWidget_37.setGeometry(QRect(40, 50, 1041, 80))
        self.horizontalLayout_38 = QHBoxLayout(self.horizontalLayoutWidget_37)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.horizontalLayoutWidget_37)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font: 600 14pt \"Segoe UI\";")

        self.horizontalLayout_38.addWidget(self.label_43)

        self.comboBox_4 = QComboBox(self.horizontalLayoutWidget_37)
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setStyleSheet(u"width:120px;\n"
"margin-right:50px;\n"
"margin-left:50px;\n"
"height:40px;\n"
"padding-left:7px;")

        self.horizontalLayout_38.addWidget(self.comboBox_4)

        self.lineEdit_38 = QLineEdit(self.horizontalLayoutWidget_37)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"margin-right:80px;")

        self.horizontalLayout_38.addWidget(self.lineEdit_38)

        self.pushButton_18 = QPushButton(self.horizontalLayoutWidget_37)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_18.setStyleSheet(u"margin-right:15px;\n"
"width:100px;\n"
"font: 600 14pt \"Segoe UI\";\n"
"heigth:60px;")

        self.horizontalLayout_38.addWidget(self.pushButton_18)

        self.tableWidget_5 = QTableWidget(self.tab_16)
        if (self.tableWidget_5.columnCount() < 5):
            self.tableWidget_5.setColumnCount(5)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setGeometry(QRect(10, 150, 911, 431))
        self.tableWidget_5.setStyleSheet(u"border:0.5px solid white;\n"
"color:white;\n"
"background-color: rgb(117, 117, 117);\n"
"font-size:12pt;\n"
"font-weigth:600;")
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(179)
        self.pushButton_19 = QPushButton(self.tab_16)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(970, 220, 181, 91))
        self.pushButton_19.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_19.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.pushButton_20 = QPushButton(self.tab_16)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(970, 400, 181, 91))
        self.pushButton_20.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_20.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.AddMember_2.addTab(self.tab_16, "")
        self.tab_18 = QWidget()
        self.tab_18.setObjectName(u"tab_18")
        self.horizontalLayoutWidget_38 = QWidget(self.tab_18)
        self.horizontalLayoutWidget_38.setObjectName(u"horizontalLayoutWidget_38")
        self.horizontalLayoutWidget_38.setGeometry(QRect(30, 20, 411, 61))
        self.horizontalLayout_39 = QHBoxLayout(self.horizontalLayoutWidget_38)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.label_44 = QLabel(self.horizontalLayoutWidget_38)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_39.addWidget(self.label_44)

        self.lineEdit_39 = QLineEdit(self.horizontalLayoutWidget_38)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_39.addWidget(self.lineEdit_39)

        self.horizontalLayoutWidget_39 = QWidget(self.tab_18)
        self.horizontalLayoutWidget_39.setObjectName(u"horizontalLayoutWidget_39")
        self.horizontalLayoutWidget_39.setGeometry(QRect(30, 340, 411, 61))
        self.horizontalLayout_40 = QHBoxLayout(self.horizontalLayoutWidget_39)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.label_45 = QLabel(self.horizontalLayoutWidget_39)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_40.addWidget(self.label_45)

        self.lineEdit_40 = QLineEdit(self.horizontalLayoutWidget_39)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_40.addWidget(self.lineEdit_40)

        self.horizontalLayoutWidget_40 = QWidget(self.tab_18)
        self.horizontalLayoutWidget_40.setObjectName(u"horizontalLayoutWidget_40")
        self.horizontalLayoutWidget_40.setGeometry(QRect(30, 260, 411, 61))
        self.horizontalLayout_41 = QHBoxLayout(self.horizontalLayoutWidget_40)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_41.setContentsMargins(0, 0, 0, 0)
        self.label_46 = QLabel(self.horizontalLayoutWidget_40)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_41.addWidget(self.label_46)

        self.lineEdit_41 = QLineEdit(self.horizontalLayoutWidget_40)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_41.addWidget(self.lineEdit_41)

        self.horizontalLayoutWidget_42 = QWidget(self.tab_18)
        self.horizontalLayoutWidget_42.setObjectName(u"horizontalLayoutWidget_42")
        self.horizontalLayoutWidget_42.setGeometry(QRect(30, 180, 411, 61))
        self.horizontalLayout_43 = QHBoxLayout(self.horizontalLayoutWidget_42)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_48 = QLabel(self.horizontalLayoutWidget_42)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_43.addWidget(self.label_48)

        self.lineEdit_43 = QLineEdit(self.horizontalLayoutWidget_42)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_43.addWidget(self.lineEdit_43)

        self.horizontalLayoutWidget_43 = QWidget(self.tab_18)
        self.horizontalLayoutWidget_43.setObjectName(u"horizontalLayoutWidget_43")
        self.horizontalLayoutWidget_43.setGeometry(QRect(30, 100, 411, 61))
        self.horizontalLayout_44 = QHBoxLayout(self.horizontalLayoutWidget_43)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.label_49 = QLabel(self.horizontalLayoutWidget_43)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_44.addWidget(self.label_49)

        self.lineEdit_44 = QLineEdit(self.horizontalLayoutWidget_43)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_44.addWidget(self.lineEdit_44)

        self.label_50 = QLabel(self.tab_18)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setGeometry(QRect(660, 10, 321, 71))
        self.horizontalLayoutWidget_44 = QWidget(self.tab_18)
        self.horizontalLayoutWidget_44.setObjectName(u"horizontalLayoutWidget_44")
        self.horizontalLayoutWidget_44.setGeometry(QRect(30, 420, 411, 61))
        self.horizontalLayout_45 = QHBoxLayout(self.horizontalLayoutWidget_44)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(0, 0, 0, 0)
        self.label_51 = QLabel(self.horizontalLayoutWidget_44)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_45.addWidget(self.label_51)

        self.lineEdit_45 = QLineEdit(self.horizontalLayoutWidget_44)
        self.lineEdit_45.setObjectName(u"lineEdit_45")
        self.lineEdit_45.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_45.addWidget(self.lineEdit_45)

        self.pushButton_21 = QPushButton(self.tab_18)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(650, 280, 291, 101))
        self.pushButton_21.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_21.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.horizontalLayoutWidget_49 = QWidget(self.tab_18)
        self.horizontalLayoutWidget_49.setObjectName(u"horizontalLayoutWidget_49")
        self.horizontalLayoutWidget_49.setGeometry(QRect(590, 180, 411, 61))
        self.horizontalLayout_50 = QHBoxLayout(self.horizontalLayoutWidget_49)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.label_53 = QLabel(self.horizontalLayoutWidget_49)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_50.addWidget(self.label_53)

        self.lineEdit_49 = QLineEdit(self.horizontalLayoutWidget_49)
        self.lineEdit_49.setObjectName(u"lineEdit_49")
        self.lineEdit_49.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_50.addWidget(self.lineEdit_49)

        self.AddMember_2.addTab(self.tab_18, "")
        self.tab_19 = QWidget()
        self.tab_19.setObjectName(u"tab_19")
        self.horizontalLayoutWidget_46 = QWidget(self.tab_19)
        self.horizontalLayoutWidget_46.setObjectName(u"horizontalLayoutWidget_46")
        self.horizontalLayoutWidget_46.setGeometry(QRect(60, 20, 1041, 80))
        self.horizontalLayout_47 = QHBoxLayout(self.horizontalLayoutWidget_46)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.horizontalLayoutWidget_46)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"font: 600 14pt \"Segoe UI\";")

        self.horizontalLayout_47.addWidget(self.label_54)

        self.comboBox_5 = QComboBox(self.horizontalLayoutWidget_46)
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.setObjectName(u"comboBox_5")
        self.comboBox_5.setStyleSheet(u"margin-right:50px;\n"
"margin-left:50px;\n"
"height:40px;\n"
"width:120px;\n"
"padding-left:7px;")

        self.horizontalLayout_47.addWidget(self.comboBox_5)

        self.lineEdit_46 = QLineEdit(self.horizontalLayoutWidget_46)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"margin-right:80px;")

        self.horizontalLayout_47.addWidget(self.lineEdit_46)

        self.pushButton_22 = QPushButton(self.horizontalLayoutWidget_46)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_22.setStyleSheet(u"margin-right:15px;\n"
"width:100px;\n"
"font: 600 14pt \"Segoe UI\";\n"
"heigth:60px;")

        self.horizontalLayout_47.addWidget(self.pushButton_22)

        self.tableWidget_6 = QTableWidget(self.tab_19)
        if (self.tableWidget_6.columnCount() < 9):
            self.tableWidget_6.setColumnCount(9)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(7, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(8, __qtablewidgetitem38)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setGeometry(QRect(0, 100, 1181, 441))
        self.tableWidget_6.setStyleSheet(u"\n"
"border:0.5px solid white;\n"
"color:white;\n"
"font-size:10pt;\n"
"font-weigth:600;")
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(130)
        self.AddMember_2.addTab(self.tab_19, "")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget_2 = QTabWidget(self.tab_4)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        self.tabWidget_2.setGeometry(QRect(0, 0, 1191, 621))
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayoutWidget_47 = QWidget(self.tab_5)
        self.horizontalLayoutWidget_47.setObjectName(u"horizontalLayoutWidget_47")
        self.horizontalLayoutWidget_47.setGeometry(QRect(20, 150, 511, 51))
        self.horizontalLayout_48 = QHBoxLayout(self.horizontalLayoutWidget_47)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.horizontalLayoutWidget_47)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_48.addWidget(self.label_55)

        self.lineEdit_47 = QLineEdit(self.horizontalLayoutWidget_47)
        self.lineEdit_47.setObjectName(u"lineEdit_47")
        self.lineEdit_47.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_48.addWidget(self.lineEdit_47)

        self.horizontalLayoutWidget_48 = QWidget(self.tab_5)
        self.horizontalLayoutWidget_48.setObjectName(u"horizontalLayoutWidget_48")
        self.horizontalLayoutWidget_48.setGeometry(QRect(20, 40, 511, 51))
        self.horizontalLayout_49 = QHBoxLayout(self.horizontalLayoutWidget_48)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(0, 0, 0, 0)
        self.label_56 = QLabel(self.horizontalLayoutWidget_48)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_49.addWidget(self.label_56)

        self.lineEdit_48 = QLineEdit(self.horizontalLayoutWidget_48)
        self.lineEdit_48.setObjectName(u"lineEdit_48")
        self.lineEdit_48.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_49.addWidget(self.lineEdit_48)

        self.horizontalLayoutWidget_50 = QWidget(self.tab_5)
        self.horizontalLayoutWidget_50.setObjectName(u"horizontalLayoutWidget_50")
        self.horizontalLayoutWidget_50.setGeometry(QRect(20, 250, 511, 281))
        self.horizontalLayout_51 = QHBoxLayout(self.horizontalLayoutWidget_50)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.horizontalLayout_51.setContentsMargins(0, 0, 0, 0)
        self.label_57 = QLabel(self.horizontalLayoutWidget_50)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_51.addWidget(self.label_57)

        self.textEdit = QTextEdit(self.horizontalLayoutWidget_50)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"font: 600 12pt \"Segoe UI\";\n"
"padding:10px;")

        self.horizontalLayout_51.addWidget(self.textEdit)

        self.horizontalLayoutWidget_51 = QWidget(self.tab_5)
        self.horizontalLayoutWidget_51.setObjectName(u"horizontalLayoutWidget_51")
        self.horizontalLayoutWidget_51.setGeometry(QRect(640, 90, 381, 51))
        self.horizontalLayout_52 = QHBoxLayout(self.horizontalLayoutWidget_51)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.horizontalLayoutWidget_51)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_52.addWidget(self.label_58)

        self.pushButton_7 = QPushButton(self.horizontalLayoutWidget_51)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_7.setStyleSheet(u"height:35px;\n"
"background-color: rgb(94, 94, 94);\n"
"color:white;\n"
"font: 700 12pt \"Segoe UI\";")

        self.horizontalLayout_52.addWidget(self.pushButton_7)

        self.pushButton_24 = QPushButton(self.tab_5)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setGeometry(QRect(700, 290, 291, 91))
        self.pushButton_24.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_24.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.tabWidget_2.addTab(self.tab_5, "")
        self.tab_20 = QWidget()
        self.tab_20.setObjectName(u"tab_20")
        self.horizontalLayoutWidget_52 = QWidget(self.tab_20)
        self.horizontalLayoutWidget_52.setObjectName(u"horizontalLayoutWidget_52")
        self.horizontalLayoutWidget_52.setGeometry(QRect(140, 20, 841, 80))
        self.horizontalLayout_53 = QHBoxLayout(self.horizontalLayoutWidget_52)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalLayout_53.setContentsMargins(0, 0, 0, 0)
        self.label_59 = QLabel(self.horizontalLayoutWidget_52)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font: 600 11pt \"Segoe UI\";")

        self.horizontalLayout_53.addWidget(self.label_59)

        self.lineEdit_51 = QLineEdit(self.horizontalLayoutWidget_52)
        self.lineEdit_51.setObjectName(u"lineEdit_51")
        self.lineEdit_51.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"width:60px;\n"
"margin-right:20px;\n"
"")

        self.horizontalLayout_53.addWidget(self.lineEdit_51)

        self.pushButton_25 = QPushButton(self.horizontalLayoutWidget_52)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_25.setStyleSheet(u"margin-right:15px;\n"
"width:100px;\n"
"font: 600 14pt \"Segoe UI\";\n"
"heigth:60px;")

        self.horizontalLayout_53.addWidget(self.pushButton_25)

        self.tableWidget_7 = QTableWidget(self.tab_20)
        if (self.tableWidget_7.columnCount() < 5):
            self.tableWidget_7.setColumnCount(5)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_7.setHorizontalHeaderItem(4, __qtablewidgetitem43)
        self.tableWidget_7.setObjectName(u"tableWidget_7")
        self.tableWidget_7.setGeometry(QRect(150, 150, 851, 271))
        self.tableWidget_7.setStyleSheet(u"border:0.5px solid white;\n"
"color:white;\n"
"background-color: rgb(117, 117, 117);\n"
"font-size:12pt;\n"
"font-weigth:600;")
        self.tableWidget_7.horizontalHeader().setDefaultSectionSize(167)
        self.pushButton_26 = QPushButton(self.tab_20)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setGeometry(QRect(410, 450, 291, 91))
        self.pushButton_26.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_26.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.tabWidget_2.addTab(self.tab_20, "")
        self.tab_21 = QWidget()
        self.tab_21.setObjectName(u"tab_21")
        self.horizontalLayoutWidget_53 = QWidget(self.tab_21)
        self.horizontalLayoutWidget_53.setObjectName(u"horizontalLayoutWidget_53")
        self.horizontalLayoutWidget_53.setGeometry(QRect(140, 10, 841, 80))
        self.horizontalLayout_54 = QHBoxLayout(self.horizontalLayoutWidget_53)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.label_60 = QLabel(self.horizontalLayoutWidget_53)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"font: 600 11pt \"Segoe UI\";")

        self.horizontalLayout_54.addWidget(self.label_60)

        self.lineEdit_52 = QLineEdit(self.horizontalLayoutWidget_53)
        self.lineEdit_52.setObjectName(u"lineEdit_52")
        self.lineEdit_52.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";\n"
"width:60px;\n"
"margin-right:20px;\n"
"")

        self.horizontalLayout_54.addWidget(self.lineEdit_52)

        self.pushButton_27 = QPushButton(self.horizontalLayoutWidget_53)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_27.setStyleSheet(u"margin-right:15px;\n"
"width:100px;\n"
"font: 600 14pt \"Segoe UI\";\n"
"heigth:60px;")

        self.horizontalLayout_54.addWidget(self.pushButton_27)

        self.tableWidget_8 = QTableWidget(self.tab_21)
        if (self.tableWidget_8.columnCount() < 6):
            self.tableWidget_8.setColumnCount(6)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget_8.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        self.tableWidget_8.setObjectName(u"tableWidget_8")
        self.tableWidget_8.setGeometry(QRect(20, 110, 1161, 461))
        self.tableWidget_8.setStyleSheet(u"border:0.5px solid white;\n"
"color:white;\n"
"background-color: rgb(117, 117, 117);\n"
"font-size:12pt;\n"
"font-weigth:600;")
        self.tableWidget_8.horizontalHeader().setDefaultSectionSize(190)
        self.tabWidget_2.addTab(self.tab_21, "")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_22 = QWidget()
        self.tab_22.setObjectName(u"tab_22")
        self.tabWidget_3 = QTabWidget(self.tab_22)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(0, 0, 1181, 621))
        self.tab_23 = QWidget()
        self.tab_23.setObjectName(u"tab_23")
        self.label_62 = QLabel(self.tab_23)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(60, 30, 831, 81))
        self.horizontalLayoutWidget_54 = QWidget(self.tab_23)
        self.horizontalLayoutWidget_54.setObjectName(u"horizontalLayoutWidget_54")
        self.horizontalLayoutWidget_54.setGeometry(QRect(70, 230, 471, 51))
        self.horizontalLayout_55 = QHBoxLayout(self.horizontalLayoutWidget_54)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalLayout_55.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.horizontalLayoutWidget_54)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_55.addWidget(self.label_63)

        self.lineEdit_53 = QLineEdit(self.horizontalLayoutWidget_54)
        self.lineEdit_53.setObjectName(u"lineEdit_53")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        font3.setBold(False)
        font3.setItalic(False)
        font3.setKerning(False)
        self.lineEdit_53.setFont(font3)
        self.lineEdit_53.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit_53.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 400 10pt \"Segoe UI\";")

        self.horizontalLayout_55.addWidget(self.lineEdit_53)

        self.horizontalLayoutWidget_55 = QWidget(self.tab_23)
        self.horizontalLayoutWidget_55.setObjectName(u"horizontalLayoutWidget_55")
        self.horizontalLayoutWidget_55.setGeometry(QRect(70, 330, 471, 51))
        self.horizontalLayout_56 = QHBoxLayout(self.horizontalLayoutWidget_55)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(0, 0, 0, 0)
        self.label_64 = QLabel(self.horizontalLayoutWidget_55)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_56.addWidget(self.label_64)

        self.lineEdit_54 = QLineEdit(self.horizontalLayoutWidget_55)
        self.lineEdit_54.setObjectName(u"lineEdit_54")
        self.lineEdit_54.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit_54.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_56.addWidget(self.lineEdit_54)

        self.horizontalLayoutWidget_56 = QWidget(self.tab_23)
        self.horizontalLayoutWidget_56.setObjectName(u"horizontalLayoutWidget_56")
        self.horizontalLayoutWidget_56.setGeometry(QRect(70, 140, 471, 51))
        self.horizontalLayout_57 = QHBoxLayout(self.horizontalLayoutWidget_56)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.horizontalLayoutWidget_56)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_57.addWidget(self.label_65)

        self.lineEdit_55 = QLineEdit(self.horizontalLayoutWidget_56)
        self.lineEdit_55.setObjectName(u"lineEdit_55")
        self.lineEdit_55.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit_55.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_57.addWidget(self.lineEdit_55)

        self.pushButton_29 = QPushButton(self.tab_23)
        self.pushButton_29.setObjectName(u"pushButton_29")
        self.pushButton_29.setGeometry(QRect(100, 410, 391, 91))
        self.pushButton_29.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_29.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.horizontalLayoutWidget_57 = QWidget(self.tab_23)
        self.horizontalLayoutWidget_57.setObjectName(u"horizontalLayoutWidget_57")
        self.horizontalLayoutWidget_57.setGeometry(QRect(670, 280, 471, 51))
        self.horizontalLayout_58 = QHBoxLayout(self.horizontalLayoutWidget_57)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.horizontalLayout_58.setContentsMargins(0, 0, 0, 0)
        self.label_66 = QLabel(self.horizontalLayoutWidget_57)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_58.addWidget(self.label_66)

        self.lineEdit_56 = QLineEdit(self.horizontalLayoutWidget_57)
        self.lineEdit_56.setObjectName(u"lineEdit_56")
        self.lineEdit_56.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit_56.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_58.addWidget(self.lineEdit_56)

        self.horizontalLayoutWidget_58 = QWidget(self.tab_23)
        self.horizontalLayoutWidget_58.setObjectName(u"horizontalLayoutWidget_58")
        self.horizontalLayoutWidget_58.setGeometry(QRect(670, 190, 471, 51))
        self.horizontalLayout_59 = QHBoxLayout(self.horizontalLayoutWidget_58)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.horizontalLayoutWidget_58)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"font: 600 12pt \"Segoe UI\";")

        self.horizontalLayout_59.addWidget(self.label_67)

        self.lineEdit_57 = QLineEdit(self.horizontalLayoutWidget_58)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.lineEdit_57.setStyleSheet(u"border:1px solid white;\n"
"border-radius:5px;\n"
"color:white;\n"
"height:40px;\n"
"padding-left:10px;\n"
"font: 700 14pt \"Segoe UI\";")

        self.horizontalLayout_59.addWidget(self.lineEdit_57)

        self.pushButton_30 = QPushButton(self.tab_23)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setGeometry(QRect(770, 370, 291, 91))
        self.pushButton_30.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_30.setStyleSheet(u"border-radius:10px;\n"
"border:2px solid white;\n"
"color:white;\n"
"background-color: rgb(68, 68, 68);\n"
"font: 700 16pt \"Segoe UI\";")
        self.tabWidget_3.addTab(self.tab_23, "")
        self.tabWidget.addTab(self.tab_22, "")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(40, 30, 221, 601))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"height:80px;\n"
"border-radius:10px;\n"
"background-color: rgb(153, 153, 153);\n"
"color:black;\n"
"font: 700 11pt \"Segoe UI\";\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icons/accueil.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"height:80px;\n"
"border-radius:10px;\n"
"background-color: rgb(153, 153, 153);\n"
"color:black;\n"
"font: 700 11pt \"Segoe UI\";\n"
"")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icons/musculation.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_4.setStyleSheet(u"height:80px;\n"
"border-radius:10px;\n"
"background-color: rgb(153, 153, 153);\n"
"color:black;\n"
"font: 700 11pt \"Segoe UI\";\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/icon/icons/entraineur.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton = QPushButton(self.verticalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"height:80px;\n"
"border-radius:10px;\n"
"background-color: rgb(153, 153, 153);\n"
"color:black;\n"
"font: 700 11pt \"Segoe UI\";\n"
"\n"
"")
        icon4 = QIcon()
        icon4.addFile(u":/icon/icons/gym.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon4)
        self.pushButton.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.pushButton)

        self.pushButton_28 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton_28.setStyleSheet(u"height:80px;\n"
"border-radius:10px;\n"
"background-color: rgb(153, 153, 153);\n"
"color:black;\n"
"font: 700 11pt \"Segoe UI\";\n"
"")
        icon5 = QIcon()
        icon5.addFile(u"icons/parametres-cog.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_28.setIcon(icon5)
        self.pushButton_28.setIconSize(QSize(30, 30))

        self.verticalLayout.addWidget(self.pushButton_28)

        MainPage.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainPage)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1479, 25))
        MainPage.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainPage)
        self.statusbar.setObjectName(u"statusbar")
        MainPage.setStatusBar(self.statusbar)

        self.retranslateUi(MainPage)

        self.tabWidget.setCurrentIndex(5)
        self.MemberTabs.setCurrentIndex(1)
        self.AddMember_2.setCurrentIndex(1)
        self.tabWidget_2.setCurrentIndex(2)
        self.tabWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPage)
    # setupUi

    def retranslateUi(self, MainPage):
        MainPage.setWindowTitle(QCoreApplication.translate("MainPage", u"MainPage", None))
        self.label.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainPage", u"Email", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainPage", u"Password", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainPage", u"Login", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainPage", u"Login", None))
        self.label_2.setText("")
        self.label_61.setText(QCoreApplication.translate("MainPage", u"GYM Management System  ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainPage", u"HomePage", None))
        self.label_3.setText(QCoreApplication.translate("MainPage", u"First Name       ", None))
        self.label_4.setText(QCoreApplication.translate("MainPage", u"Second Name  ", None))
        self.label_5.setText(QCoreApplication.translate("MainPage", u"Age                 ", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("MainPage", u" Older than 10 years", None))
        self.label_6.setText(QCoreApplication.translate("MainPage", u"Phone             ", None))
        self.label_7.setText(QCoreApplication.translate("MainPage", u"Gender            ", None))
        self.lineEdit_7.setPlaceholderText(QCoreApplication.translate("MainPage", u"Enter \"M\" or \"F\"", None))
        self.label_8.setText(QCoreApplication.translate("MainPage", u"Email               ", None))
        self.label_9.setText(QCoreApplication.translate("MainPage", u"Sessions PerWeek", None))
        self.label_11.setText(QCoreApplication.translate("MainPage", u"Duration  ", None))
        self.comboBox_6.setItemText(0, QCoreApplication.translate("MainPage", u"1 month", None))
        self.comboBox_6.setItemText(1, QCoreApplication.translate("MainPage", u"3 months", None))
        self.comboBox_6.setItemText(2, QCoreApplication.translate("MainPage", u"6 months", None))
        self.comboBox_6.setItemText(3, QCoreApplication.translate("MainPage", u"1 year", None))

        self.pushButton_6.setText(QCoreApplication.translate("MainPage", u"ADD", None))
        self.MemberTabs.setTabText(self.MemberTabs.indexOf(self.tab_6), QCoreApplication.translate("MainPage", u"Add Members              ", None))
        self.label_19.setText(QCoreApplication.translate("MainPage", u"Search for the member : ", None))
        self.label_20.setText(QCoreApplication.translate("MainPage", u"Search by : ", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainPage", u"First Name", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainPage", u"Second Name", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainPage", u"Phone Number", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainPage", u"Email", None))

        self.pushButton_8.setText(QCoreApplication.translate("MainPage", u"Search", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainPage", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainPage", u"First Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainPage", u"Second Name", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainPage", u"Age", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainPage", u"Phone", None));
        self.pushButton_9.setText(QCoreApplication.translate("MainPage", u"UPDATE", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainPage", u"DELETE", None))
        self.MemberTabs.setTabText(self.MemberTabs.indexOf(self.tab_8), QCoreApplication.translate("MainPage", u"Update/Delete Members", None))
        self.label_21.setText(QCoreApplication.translate("MainPage", u"First Name     ", None))
        self.label_23.setText(QCoreApplication.translate("MainPage", u"Phone           ", None))
        self.label_24.setText(QCoreApplication.translate("MainPage", u"Email             ", None))
        self.lineEdit_23.setPlaceholderText(QCoreApplication.translate("MainPage", u"Write it again", None))
        self.label_25.setText(QCoreApplication.translate("MainPage", u"Gender          ", None))
        self.lineEdit_24.setPlaceholderText(QCoreApplication.translate("MainPage", u"Write it again", None))
        self.label_26.setText(QCoreApplication.translate("MainPage", u"Age               ", None))
        self.label_27.setText(QCoreApplication.translate("MainPage", u"Second Name", None))
        self.label_22.setText(QCoreApplication.translate("MainPage", u"Sessions Management", None))
        self.label_28.setText(QCoreApplication.translate("MainPage", u"Sessions PerWeek", None))
        self.lineEdit_21.setText("")
        self.lineEdit_21.setPlaceholderText(QCoreApplication.translate("MainPage", u"Write it again", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainPage", u"UPDATE", None))
        self.label_12.setText(QCoreApplication.translate("MainPage", u"Duration  ", None))
        self.comboBox_7.setItemText(0, QCoreApplication.translate("MainPage", u"1 month", None))
        self.comboBox_7.setItemText(1, QCoreApplication.translate("MainPage", u"3 months", None))
        self.comboBox_7.setItemText(2, QCoreApplication.translate("MainPage", u"6 months", None))
        self.comboBox_7.setItemText(3, QCoreApplication.translate("MainPage", u"1 year", None))

        self.MemberTabs.setTabText(self.MemberTabs.indexOf(self.tab_9), QCoreApplication.translate("MainPage", u"Change member information", None))
        self.label_31.setText(QCoreApplication.translate("MainPage", u"Search by : ", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainPage", u"First Name", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainPage", u"Second Name", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainPage", u"Phone Number", None))
        self.comboBox_2.setItemText(3, QCoreApplication.translate("MainPage", u"Email", None))

        self.pushButton_12.setText(QCoreApplication.translate("MainPage", u"Search", None))
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainPage", u"ID", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainPage", u"First Name", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainPage", u"Second Name", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainPage", u"Age", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainPage", u"Gender", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainPage", u"Email", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainPage", u"Phone", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainPage", u"Sessions/Week", None));
        ___qtablewidgetitem13 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainPage", u"Payement $", None));
        self.MemberTabs.setTabText(self.MemberTabs.indexOf(self.tab_10), QCoreApplication.translate("MainPage", u"Search for members data", None))
        self.label_32.setText(QCoreApplication.translate("MainPage", u"Search Memeber : ", None))
        self.comboBox_3.setItemText(0, QCoreApplication.translate("MainPage", u"First Name", None))
        self.comboBox_3.setItemText(1, QCoreApplication.translate("MainPage", u"Second Name", None))
        self.comboBox_3.setItemText(2, QCoreApplication.translate("MainPage", u"Phone Number", None))
        self.comboBox_3.setItemText(3, QCoreApplication.translate("MainPage", u"Email", None))

        self.pushButton_14.setText(QCoreApplication.translate("MainPage", u"Search", None))
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainPage", u"ID", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainPage", u"First Name", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainPage", u"Second Name", None));
        ___qtablewidgetitem17 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainPage", u"Age", None));
        ___qtablewidgetitem18 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainPage", u"Phone", None));
        self.label_33.setText(QCoreApplication.translate("MainPage", u"Search Coach : ", None))
        self.comboBox_8.setItemText(0, QCoreApplication.translate("MainPage", u"First Name", None))
        self.comboBox_8.setItemText(1, QCoreApplication.translate("MainPage", u"Second Name", None))
        self.comboBox_8.setItemText(2, QCoreApplication.translate("MainPage", u"Phone Number", None))
        self.comboBox_8.setItemText(3, QCoreApplication.translate("MainPage", u"Email", None))

        self.pushButton_15.setText(QCoreApplication.translate("MainPage", u"Search", None))
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainPage", u"ID", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainPage", u"First Name", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainPage", u"Second Name", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainPage", u"Phone", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainPage", u"Working days", None));
        self.pushButton_16.setText(QCoreApplication.translate("MainPage", u"ASSIGN", None))
        self.MemberTabs.setTabText(self.MemberTabs.indexOf(self.tab_17), QCoreApplication.translate("MainPage", u"Coach Assignement             ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainPage", u"Members", None))
        self.label_34.setText(QCoreApplication.translate("MainPage", u"First Name       ", None))
        self.label_35.setText(QCoreApplication.translate("MainPage", u"Second Name  ", None))
        self.label_36.setText(QCoreApplication.translate("MainPage", u"Age                 ", None))
        self.label_37.setText(QCoreApplication.translate("MainPage", u"Phone             ", None))
        self.label_39.setText(QCoreApplication.translate("MainPage", u"Email               ", None))
        self.label_40.setText(QCoreApplication.translate("MainPage", u"Days PerWeek", None))
        self.label_41.setText(QCoreApplication.translate("MainPage", u"Payement       ", None))
        self.pushButton_17.setText(QCoreApplication.translate("MainPage", u"ADD", None))
        self.AddMember_2.setTabText(self.AddMember_2.indexOf(self.tab_15), QCoreApplication.translate("MainPage", u"Add Coach              ", None))
        self.label_42.setText(QCoreApplication.translate("MainPage", u"Search for the member : ", None))
        self.label_43.setText(QCoreApplication.translate("MainPage", u"Search by : ", None))
        self.comboBox_4.setItemText(0, QCoreApplication.translate("MainPage", u"First Name", None))
        self.comboBox_4.setItemText(1, QCoreApplication.translate("MainPage", u"Second Name", None))
        self.comboBox_4.setItemText(2, QCoreApplication.translate("MainPage", u"Phone Number", None))
        self.comboBox_4.setItemText(3, QCoreApplication.translate("MainPage", u"Email", None))

        self.pushButton_18.setText(QCoreApplication.translate("MainPage", u"Search", None))
        ___qtablewidgetitem24 = self.tableWidget_5.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainPage", u"ID", None));
        ___qtablewidgetitem25 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainPage", u"First Name", None));
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainPage", u"Second Name", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainPage", u"Phone", None));
        ___qtablewidgetitem28 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainPage", u"Working Days", None));
        self.pushButton_19.setText(QCoreApplication.translate("MainPage", u"UPDATE", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainPage", u"DELETE", None))
        self.AddMember_2.setTabText(self.AddMember_2.indexOf(self.tab_16), QCoreApplication.translate("MainPage", u"Update/Delete Coach", None))
        self.label_44.setText(QCoreApplication.translate("MainPage", u"First Name     ", None))
        self.label_45.setText(QCoreApplication.translate("MainPage", u"Phone           ", None))
        self.label_46.setText(QCoreApplication.translate("MainPage", u"Email             ", None))
        self.label_48.setText(QCoreApplication.translate("MainPage", u"Age               ", None))
        self.label_49.setText(QCoreApplication.translate("MainPage", u"Second Name", None))
        self.label_50.setText(QCoreApplication.translate("MainPage", u"Sessions Management", None))
        self.label_51.setText(QCoreApplication.translate("MainPage", u"Days PerWeek", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainPage", u"UPDATE", None))
        self.label_53.setText(QCoreApplication.translate("MainPage", u"Payement      ", None))
        self.AddMember_2.setTabText(self.AddMember_2.indexOf(self.tab_18), QCoreApplication.translate("MainPage", u"Change Coach information", None))
        self.label_54.setText(QCoreApplication.translate("MainPage", u"Search by : ", None))
        self.comboBox_5.setItemText(0, QCoreApplication.translate("MainPage", u"First Name", None))
        self.comboBox_5.setItemText(1, QCoreApplication.translate("MainPage", u"Second Name", None))
        self.comboBox_5.setItemText(2, QCoreApplication.translate("MainPage", u"Phone Number", None))
        self.comboBox_5.setItemText(3, QCoreApplication.translate("MainPage", u"Email", None))

        self.pushButton_22.setText(QCoreApplication.translate("MainPage", u"Search", None))
        ___qtablewidgetitem29 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainPage", u"ID", None));
        ___qtablewidgetitem30 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainPage", u"First Name", None));
        ___qtablewidgetitem31 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainPage", u"Second Name", None));
        ___qtablewidgetitem32 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainPage", u"Gender", None));
        ___qtablewidgetitem33 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainPage", u"Phone", None));
        ___qtablewidgetitem34 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainPage", u"Email", None));
        ___qtablewidgetitem35 = self.tableWidget_6.horizontalHeaderItem(6)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainPage", u"Sessions/Week", None));
        ___qtablewidgetitem36 = self.tableWidget_6.horizontalHeaderItem(7)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainPage", u"Payement", None));
        ___qtablewidgetitem37 = self.tableWidget_6.horizontalHeaderItem(8)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainPage", u"Trainees", None));
        self.AddMember_2.setTabText(self.AddMember_2.indexOf(self.tab_19), QCoreApplication.translate("MainPage", u"Search for Coaches data", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QCoreApplication.translate("MainPage", u"Staff        ", None))
        self.label_55.setText(QCoreApplication.translate("MainPage", u"Cost           ", None))
        self.label_56.setText(QCoreApplication.translate("MainPage", u"Name         ", None))
        self.label_57.setText(QCoreApplication.translate("MainPage", u"Description ", None))
        self.label_58.setText(QCoreApplication.translate("MainPage", u"Image         ", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainPage", u"Upload Image", None))
        self.pushButton_24.setText(QCoreApplication.translate("MainPage", u"ADD", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_5), QCoreApplication.translate("MainPage", u"Add Machines", None))
        self.label_59.setText(QCoreApplication.translate("MainPage", u"Equipement Name", None))
        self.pushButton_25.setText(QCoreApplication.translate("MainPage", u"Search", None))
        ___qtablewidgetitem38 = self.tableWidget_7.horizontalHeaderItem(0)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainPage", u"ID", None));
        ___qtablewidgetitem39 = self.tableWidget_7.horizontalHeaderItem(1)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainPage", u"Name", None));
        ___qtablewidgetitem40 = self.tableWidget_7.horizontalHeaderItem(2)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainPage", u"Description", None));
        ___qtablewidgetitem41 = self.tableWidget_7.horizontalHeaderItem(3)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainPage", u"cost", None));
        ___qtablewidgetitem42 = self.tableWidget_7.horizontalHeaderItem(4)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainPage", u"bring date", None));
        self.pushButton_26.setText(QCoreApplication.translate("MainPage", u"DELETE", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_20), QCoreApplication.translate("MainPage", u"Drop Machine", None))
        self.label_60.setText(QCoreApplication.translate("MainPage", u"Equipement Name", None))
        self.pushButton_27.setText(QCoreApplication.translate("MainPage", u"Search", None))
        ___qtablewidgetitem43 = self.tableWidget_8.horizontalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainPage", u"ID", None));
        ___qtablewidgetitem44 = self.tableWidget_8.horizontalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainPage", u"Name", None));
        ___qtablewidgetitem45 = self.tableWidget_8.horizontalHeaderItem(2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainPage", u"Description", None));
        ___qtablewidgetitem46 = self.tableWidget_8.horizontalHeaderItem(3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainPage", u"Cost", None));
        ___qtablewidgetitem47 = self.tableWidget_8.horizontalHeaderItem(4)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainPage", u"Bring date", None));
        ___qtablewidgetitem48 = self.tableWidget_8.horizontalHeaderItem(5)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainPage", u"Image", None));
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_21), QCoreApplication.translate("MainPage", u"Display Equipements", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainPage", u"Equipements", None))
        self.label_62.setText(QCoreApplication.translate("MainPage", u"Update the Admin password & email  : ", None))
        self.label_63.setText(QCoreApplication.translate("MainPage", u"New Password  ", None))
        self.lineEdit_53.setPlaceholderText(QCoreApplication.translate("MainPage", u">8 chars containing numbers", None))
        self.label_64.setText(QCoreApplication.translate("MainPage", u"Confirmation    ", None))
        self.label_65.setText(QCoreApplication.translate("MainPage", u"Curr Password  ", None))
        self.pushButton_29.setText(QCoreApplication.translate("MainPage", u"UPDATE PASSWORD", None))
        self.label_66.setText(QCoreApplication.translate("MainPage", u"New email    ", None))
        self.label_67.setText(QCoreApplication.translate("MainPage", u"Curr email    ", None))
        self.pushButton_30.setText(QCoreApplication.translate("MainPage", u"UPDATE EMAIL", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_23), QCoreApplication.translate("MainPage", u"Update password && email", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_22), QCoreApplication.translate("MainPage", u"Settings", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainPage", u"Home Page", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainPage", u"Members", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainPage", u"Staff", None))
        self.pushButton.setText(QCoreApplication.translate("MainPage", u"Equipements", None))
        self.pushButton_28.setText(QCoreApplication.translate("MainPage", u"Setting", None))
    # retranslateUi

