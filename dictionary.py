from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import search_word
import text_to_speech

class Ui_Form(object):

    def recent(self,txt):
        try:
            dbcon = sqlite3.connect('history.db')
            word_curs = dbcon.cursor()
            word_curs.execute("INSERT INTO WORDS(recent_words) VALUES(?);",[txt])
            dbcon.commit()
        except Exception as e:
            print(e)

    def showRecent(self):
        try:
            dbcon = sqlite3.connect('history.db')
            word_curs = dbcon.cursor()
            word_curs.execute("SELECT recent_words FROM WORDS")
            total = ""
            count = 1
            result = word_curs.fetchall()
            for i in result:
                i = "<h4>%d) %s" %(count,i[0])
                total = total + i
                count += 1
            self.textBrowser_3.setText(total)
        except Exception as e:
            print(e)

    def deleteData(self):
        try:
            dbcon = sqlite3.connect('history.db')
            word_curs = dbcon.cursor()
            word_curs.execute("DELETE FROM WORDS")
            dbcon.commit()
        except Exception as e:
            print(e)

            
    def find(self):
        total = ""
        txt = self.lineEdit.text()
        find_word = search_word.search_word(txt)
        if type(find_word) == list:
            for i in find_word:
                i = "<h4><b>--%s</b><br>" % i
                total = total + i
            self.textBrowser.setText(total)
            self.recent(txt)
        else:
            find_word = '<span style="color: red"><span style="font-size: 12px">%s</span></span>' % find_word
            self.textBrowser_2.setText(find_word)

    def speech(self):
        txt = self.lineEdit.text()
        text_to_speech.speech_conversion(txt)

        
    def setupUi(self, Form):
        Form.setObjectName("Dictionary")
        Form.setFixedSize(640, 480)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 641, 491))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("background.jpg"))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(410, 30, 211, 61))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("brand.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutWidget = QtWidgets.QWidget(Form)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(70, 60, 231, 27))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 90, 231, 80))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.search.setFont(font)
        self.search.setObjectName("search")
        self.horizontalLayout.addWidget(self.search)
        self.clear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.clear.setFont(font)
        self.clear.setObjectName("clear")
        self.horizontalLayout.addWidget(self.clear)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(10, 220, 451, 241))
        self.textBrowser.setObjectName("textBrowser")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(360, 110, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setTextFormat(QtCore.Qt.RichText)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(70, 30, 171, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setObjectName("label_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setGeometry(QtCore.QRect(355, 140, 241, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.sound = QtWidgets.QPushButton(Form)
        self.sound.setGeometry(QtCore.QRect(310, 60, 31, 31))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("speaker.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sound.setIcon(icon)
        self.sound.setObjectName("sound")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(490, 190, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.RichText)
        self.label_6.setObjectName("label_6")
        self.showData = QtWidgets.QPushButton(Form)
        self.showData.setGeometry(QtCore.QRect(480, 430, 61, 23))
        self.showData.setObjectName("showData")
        self.clearHistory = QtWidgets.QPushButton(Form)
        self.clearHistory.setGeometry(QtCore.QRect(560, 430, 71, 23))
        self.clearHistory.setObjectName("clearHistory")
        self.textBrowser_3 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_3.setGeometry(QtCore.QRect(480, 220, 151, 201))
        self.textBrowser_3.setObjectName("textBrowser_3")

        self.retranslateUi(Form)
        self.clear.clicked.connect(self.lineEdit.clear)
        self.clear.clicked.connect(self.textBrowser_2.clear)
        self.clearHistory.clicked.connect(self.textBrowser_3.clear)
        self.clearHistory.clicked.connect(self.deleteData)
        self.search.clicked.connect(self.textBrowser_2.clear)
        self.search.clicked.connect(self.textBrowser.clear)
        self.search.clicked.connect(self.find)
        self.sound.clicked.connect(self.speech)
        self.showData.clicked.connect(self.showRecent)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dictionary by AJ Group"))
        self.search.setText(_translate("Form", "Search"))
        self.clear.setText(_translate("Form", "Clear"))
        self.label_3.setToolTip(_translate("Form", "<html><head/><body><p>Define</p></body></html>"))
        self.label_3.setText(_translate("Form", "Meanning :-"))
        self.label_4.setToolTip(_translate("Form", "<html><head/><body><p>Here you will get suggetion for incorrect spelling :)</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#ffaa00;\">Suggestion :-</span></p></body></html>"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" color:#00ffff;\">Search for a word :-</span></p></body></html>"))
        self.label_6.setToolTip(_translate("Form", "<html><head/><body><p>Shows History</p></body></html>"))
        self.label_6.setText(_translate("Form", "Recent words :-"))
        self.showData.setText(_translate("Form", "Show"))
        self.clearHistory.setText(_translate("Form", "Clear History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
