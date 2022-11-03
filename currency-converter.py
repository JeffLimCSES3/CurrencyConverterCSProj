# Form implementation generated from reading ui file 'currency-converter.ui'
# Created by: PyQt5 UI code generator 5.15.7

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon

import requests
import sys

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Currency Converter")
        MainWindow.setFixedSize(255, 525) #Fixed window size
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 255, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        self.startingAmountInput = QtWidgets.QTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.startingAmountInput.setFont(font)
        self.startingAmountInput.setObjectName("startingAmountInput")
        self.startingAmountInput.setGeometry(QtCore.QRect(10, 80, 221, 45))

        self.exchangeCurrencyOutput = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.exchangeCurrencyOutput.setFont(font)
        self.exchangeCurrencyOutput.setObjectName("exchangeCurrencyOutput")
        self.exchangeCurrencyOutput.setGeometry(QtCore.QRect(10, 165, 231, 51))

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

        self.decimalPlaceCounterLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.decimalPlaceCounterLabel.setFont(font)
        self.decimalPlaceCounterLabel.setGeometry(QtCore.QRect(10, 345, 231, 30))
        
        self.decimalPlaceCounter = QtWidgets.QSpinBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.decimalPlaceCounter.setFont(font)
        self.decimalPlaceCounter.setMaximum(4)
        self.decimalPlaceCounter.setGeometry(QtCore.QRect(10, 380, 231, 30))

        self.exchangeRateLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.exchangeRateLabel.setFont(font)
        self.exchangeRateLabel.setGeometry(QtCore.QRect(10, 415, 231, 51))

        self.creditsLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(6)
        self.creditsLabel.setFont(font)
        self.creditsLabel.setGeometry(QtCore.QRect(10, 450, 231, 51))

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
        MainWindow.setWindowTitle(_translate("Currency Converter", "Currency Converter"))
        
        self.label.setText(_translate("Currency Converter", "Currency Converter"))
        self.exchangeCurrencyOutput.setText(_translate("Currency Converter", "  "))
        self.convertCurrencyButton.setText(_translate("Currency Converter", "Convert"))
        self.swapCurrenciesButton.setText(_translate("Currency Converter", "ɅV"))
        self.exchangeRateLabel.setText(_translate("Currency Converter", ""))
        self.decimalPlaceCounterLabel.setText(_translate("Currency Converter", "Number of decimal places to show: "))
        self.creditsLabel.setText(_translate("Currency Converter", "Made by Jeff Lim 10B for Computer Science Project 2022-2023"))

        #Default starting currency set to IDR
        self.startingCurrencyInputDropDown.setItemText(0, _translate("Currency Converter", "IDR")) 
        self.startingCurrencyInputDropDown.setItemText(1, _translate("Currency Converter", "USD"))
        self.startingCurrencyInputDropDown.setItemText(2, _translate("Currency Converter", "AED"))
        self.startingCurrencyInputDropDown.setItemText(3, _translate("Currency Converter", "AUD"))
        self.startingCurrencyInputDropDown.setItemText(4, _translate("Currency Converter", "CAD"))
        self.startingCurrencyInputDropDown.setItemText(5, _translate("Currency Converter", "CHF"))
        self.startingCurrencyInputDropDown.setItemText(6, _translate("Currency Converter", "EUR"))
        self.startingCurrencyInputDropDown.setItemText(7, _translate("Currency Converter", "GBP"))
        self.startingCurrencyInputDropDown.setItemText(8, _translate("Currency Converter", "HKD"))
        self.startingCurrencyInputDropDown.setItemText(9, _translate("Currency Converter", "JPY"))
        self.startingCurrencyInputDropDown.setItemText(10, _translate("Currency Converter", "SGD"))

        #Default exchange currency set to USD
        self.exchangeCurrencyInputDropdown.setItemText(0, _translate("Currency Converter", "USD")) 
        self.exchangeCurrencyInputDropdown.setItemText(1, _translate("Currency Converter", "IDR"))
        self.exchangeCurrencyInputDropdown.setItemText(2, _translate("Currency Converter", "AED"))
        self.exchangeCurrencyInputDropdown.setItemText(3, _translate("Currency Converter", "AUD"))
        self.exchangeCurrencyInputDropdown.setItemText(4, _translate("Currency Converter", "CAD"))
        self.exchangeCurrencyInputDropdown.setItemText(5, _translate("Currency Converter", "CHF"))
        self.exchangeCurrencyInputDropdown.setItemText(6, _translate("Currency Converter", "EUR"))
        self.exchangeCurrencyInputDropdown.setItemText(7, _translate("Currency Converter", "GBP"))
        self.exchangeCurrencyInputDropdown.setItemText(8, _translate("Currency Converter", "HKD"))
        self.exchangeCurrencyInputDropdown.setItemText(9, _translate("Currency Converter", "JPY"))
        self.exchangeCurrencyInputDropdown.setItemText(10, _translate("Currency Converter", "SGD"))

    #Code related to converting the currency
    def convert_currency_button_pressed(self):
        
        starting_currency = self.startingCurrencyInputDropDown.currentText() #Starting currency
        exchange_currency = self.exchangeCurrencyInputDropdown.currentText() #Exchange currency
    
        url = requests.get('https://v6.exchangerate-api.com/v6/115fa7e93047be6a26a1c328/pair/' + starting_currency + '/' + exchange_currency)
        data = url.json()
        
        starting_amount = self.startingAmountInput.toPlainText() #Reads the input of the starting amount
    
        currency_exchange_value = data['conversion_rate'] #Gets the currency exchange rate
        currency_exchange_output_text = str(round(float(float(starting_amount) * float(currency_exchange_value)), self.decimalPlaceCounter.value()))

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
        data = url.json()
        
        self.startingAmountInput.setText(self.exchangeCurrencyOutput.text()) #Sets the text inside the starting amount input as the value of the exchanged amount
        starting_amount = self.exchangeCurrencyOutput.text() #Sets the starting amount as the previous exchanged amount
    
        currency_exchange_value = data['conversion_rate'] #Gets the currency exchange rate
        currency_exchange_output_text = str(round(float(float(starting_amount) * float(currency_exchange_value)), self.decimalPlaceCounter.value()))

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
    app.setWindowIcon(QIcon('logo.png'))
    
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())