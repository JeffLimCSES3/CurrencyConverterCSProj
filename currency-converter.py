# Form implementation generated from reading ui file 'currency-converter.ui'
# Created by: PyQt5 UI code generator 5.15.7

from tracemalloc import start
from PyQt5 import QtCore, QtGui, QtWidgets

import requests
#Features to add: counter box to increase dps (max 5 dp)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(255, 460) #Fixed window size

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 255, 31))

        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.startingAmountInput = QtWidgets.QTextEdit(self.centralwidget)
        self.startingAmountInput.setGeometry(QtCore.QRect(10, 80, 221, 41))

        font = QtGui.QFont()
        font.setPointSize(14)
        self.startingAmountInput.setFont(font)
        self.startingAmountInput.setObjectName("startingAmountInput")
        self.exchangeCurrencyOutput = QtWidgets.QLabel(self.centralwidget)
        self.exchangeCurrencyOutput.setGeometry(QtCore.QRect(10, 170, 241, 31))

        font = QtGui.QFont()
        font.setPointSize(20)
        self.exchangeCurrencyOutput.setFont(font)
        self.exchangeCurrencyOutput.setObjectName("exchangeCurrencyOutput")

        #Convert currency button 
        self.convertCurrencyButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.convert_currency_button_pressed())

        self.convertCurrencyButton.setGeometry(QtCore.QRect(10, 230, 231, 51))

        font = QtGui.QFont()
        font.setPointSize(19)
        self.convertCurrencyButton.setFont(font)
        self.convertCurrencyButton.setObjectName("convertCurrencyButton")

        #Switch currencies button
        self.swapCurrenciesButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda: self.switch_currency_button_pressed())

        self.swapCurrenciesButton.setGeometry(QtCore.QRect(10, 290, 231, 51))

        font = QtGui.QFont()
        font.setPointSize(19)
        self.swapCurrenciesButton.setFont(font)
        self.swapCurrenciesButton.setObjectName("swapCurrenciesButton")

        
        self.exchangeRateLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.exchangeRateLabel.setFont(font)
        self.exchangeRateLabel.setGeometry(QtCore.QRect(10, 340, 231, 51))

        self.creditsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.creditsLabel.setFont(font)
        self.creditsLabel.setGeometry(QtCore.QRect(10, 400, 231, 51))

        self.startingCurrencyInputDropDown = QtWidgets.QComboBox(self.centralwidget)
        self.startingCurrencyInputDropDown.setGeometry(QtCore.QRect(10, 50, 221, 22))
        self.startingCurrencyInputDropDown.setObjectName("startingCurrencyInputDropDown")
        self.startingCurrencyInputDropDown.addItem("")
        self.startingCurrencyInputDropDown.addItem("")
        self.startingCurrencyInputDropDown.addItem("")
        self.startingCurrencyInputDropDown.addItem("")
        self.startingCurrencyInputDropDown.addItem("")
        self.startingCurrencyInputDropDown.addItem("")
        self.startingCurrencyInputDropDown.addItem("")
        self.startingCurrencyInputDropDown.addItem("")
        self.startingCurrencyInputDropDown.addItem("")
        self.startingCurrencyInputDropDown.addItem("")
        self.startingCurrencyInputDropDown.addItem("")

        self.exchangeCurrencyInputDropdown = QtWidgets.QComboBox(self.centralwidget)
        self.exchangeCurrencyInputDropdown.setGeometry(QtCore.QRect(10, 130, 221, 22))
        self.exchangeCurrencyInputDropdown.setObjectName("exchangeCurrencyInputDropdown")
        self.exchangeCurrencyInputDropdown.addItem("")
        self.exchangeCurrencyInputDropdown.addItem("")
        self.exchangeCurrencyInputDropdown.addItem("")
        self.exchangeCurrencyInputDropdown.addItem("")
        self.exchangeCurrencyInputDropdown.addItem("")
        self.exchangeCurrencyInputDropdown.addItem("")
        self.exchangeCurrencyInputDropdown.addItem("")
        self.exchangeCurrencyInputDropdown.addItem("")
        self.exchangeCurrencyInputDropdown.addItem("")
        self.exchangeCurrencyInputDropdown.addItem("")
        self.exchangeCurrencyInputDropdown.addItem("")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 258, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Currency Converter"))
        self.exchangeCurrencyOutput.setText(_translate("MainWindow", "  "))
        self.convertCurrencyButton.setText(_translate("MainWindow", "Convert"))
        self.swapCurrenciesButton.setText(_translate("MainWindow", "ɅV"))
        self.exchangeRateLabel.setText(_translate("MainWindow", ""))
        self.creditsLabel.setText(_translate("MainWindow", "Made by Jeff Lim 10B for Computer Science Project 2022-2023"))

        #Default starting currency set to IDR
        self.startingCurrencyInputDropDown.setItemText(0, _translate("MainWindow", "IDR")) 
        self.startingCurrencyInputDropDown.setItemText(1, _translate("MainWindow", "USD"))
        self.startingCurrencyInputDropDown.setItemText(2, _translate("MainWindow", "AED"))
        self.startingCurrencyInputDropDown.setItemText(3, _translate("MainWindow", "AUD"))
        self.startingCurrencyInputDropDown.setItemText(4, _translate("MainWindow", "CAD"))
        self.startingCurrencyInputDropDown.setItemText(5, _translate("MainWindow", "CHF"))
        self.startingCurrencyInputDropDown.setItemText(6, _translate("MainWindow", "EUR"))
        self.startingCurrencyInputDropDown.setItemText(7, _translate("MainWindow", "GBP"))
        self.startingCurrencyInputDropDown.setItemText(8, _translate("MainWindow", "HKD"))
        self.startingCurrencyInputDropDown.setItemText(9, _translate("MainWindow", "JPY"))
        self.startingCurrencyInputDropDown.setItemText(10, _translate("MainWindow", "SGD"))

        #Default exchange currency set to USD
        self.exchangeCurrencyInputDropdown.setItemText(0, _translate("MainWindow", "USD")) 
        self.exchangeCurrencyInputDropdown.setItemText(1, _translate("MainWindow", "IDR"))
        self.exchangeCurrencyInputDropdown.setItemText(2, _translate("MainWindow", "AED"))
        self.exchangeCurrencyInputDropdown.setItemText(3, _translate("MainWindow", "AUD"))
        self.exchangeCurrencyInputDropdown.setItemText(4, _translate("MainWindow", "CAD"))
        self.exchangeCurrencyInputDropdown.setItemText(5, _translate("MainWindow", "CHF"))
        self.exchangeCurrencyInputDropdown.setItemText(6, _translate("MainWindow", "EUR"))
        self.exchangeCurrencyInputDropdown.setItemText(7, _translate("MainWindow", "GBP"))
        self.exchangeCurrencyInputDropdown.setItemText(8, _translate("MainWindow", "HKD"))
        self.exchangeCurrencyInputDropdown.setItemText(9, _translate("MainWindow", "JPY"))
        self.exchangeCurrencyInputDropdown.setItemText(10, _translate("MainWindow", "SGD"))

    #Code related to converting the currency
    def convert_currency_button_pressed(self):
        
        starting_currency = self.startingCurrencyInputDropDown.currentText() #Starting currency
        exchange_currency = self.exchangeCurrencyInputDropdown.currentText() #Exchange currency
    
        url = requests.get('https://v6.exchangerate-api.com/v6/115fa7e93047be6a26a1c328/pair/' + starting_currency + '/' + exchange_currency)
        data = url.json()
        
        starting_amount = self.startingAmountInput.toPlainText() #Reads the input of the starting amount
    
        currency_exchange_value = data['conversion_rate'] #Gets the currency exchange rate
        currency_exchange_output_text = str(round(float(float(starting_amount) * float(currency_exchange_value)), 4))

        #Exchange rate label
        exchange_rate_url = requests.get('https://v6.exchangerate-api.com/v6/115fa7e93047be6a26a1c328/pair/' + exchange_currency + '/' + starting_currency)
        exchange_rate_data = exchange_rate_url.json()
        exchange_rate_value = exchange_rate_data['conversion_rate']

        exchange_rate = str(round(float(exchange_rate_value), 4))

        #Output text
        self.exchangeRateLabel.setText("1 " + exchange_currency + " ---> " + starting_currency + " " + exchange_rate) #Sets exchange rate label text
        self.exchangeCurrencyOutput.setText(currency_exchange_output_text) #Sets the calculated value of the currency exchanged

    #Code related to switching positions of the currency to change 
    def switch_currency_button_pressed(self):
        
        temp = self.startingCurrencyInputDropDown.currentText() #Create a temp variable to store the value of the starting currency

        self.startingCurrencyInputDropDown.setCurrentText(self.exchangeCurrencyInputDropdown.currentText()) #Changes the starting currency with the exchange currency
        self.exchangeCurrencyInputDropdown.setCurrentText(temp) #Changes the exchange currency with the starting currency through the temp variable

        starting_currency = self.startingCurrencyInputDropDown.currentText() #Starting currency
        exchange_currency = self.exchangeCurrencyInputDropdown.currentText() #Exchange currency
    
        url = requests.get('https://v6.exchangerate-api.com/v6/115fa7e93047be6a26a1c328/pair/' + starting_currency + '/' + exchange_currency)

        # Making our request
        data = url.json()
        
        self.startingAmountInput.setText(self.exchangeCurrencyOutput.text()) #Sets the text inside the starting amount input as the value of the exchanged amount
        starting_amount = self.exchangeCurrencyOutput.text() #Sets the starting amount as the previous exchanged amount
    
        currency_exchange_value = data['conversion_rate'] #Gets the currency exchange rate
        currency_exchange_output_text = str(round(float(float(starting_amount) * float(currency_exchange_value)), 4))

        #Exchange rate label
        exchange_rate_url = requests.get('https://v6.exchangerate-api.com/v6/115fa7e93047be6a26a1c328/pair/' + exchange_currency + '/' + starting_currency)
        exchange_rate_data = exchange_rate_url.json()
        exchange_rate_value = exchange_rate_data['conversion_rate']

        exchange_rate = str(round(float(exchange_rate_value), 4))

        #Output text
        self.exchangeRateLabel.setText("1 " + exchange_currency + " ---> " + starting_currency + " " + exchange_rate)
        self.exchangeCurrencyOutput.setText(currency_exchange_output_text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())