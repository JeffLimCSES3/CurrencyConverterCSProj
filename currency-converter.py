# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'currency-converter.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

import requests
url = 'https://v6.exchangerate-api.com/v6/115fa7e93047be6a26a1c328/latest/USD'

# Making our request
response = requests.get(url)
data = response.json()
print(data)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(258, 419)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.startingCurrencyInput = QtWidgets.QTextEdit(self.centralwidget)
        self.startingCurrencyInput.setGeometry(QtCore.QRect(10, 80, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startingCurrencyInput.setFont(font)
        self.startingCurrencyInput.setObjectName("startingCurrencyInput")
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
        self.swapCurrenciesButton = QtWidgets.QPushButton(self.centralwidget)
        self.swapCurrenciesButton.setGeometry(QtCore.QRect(10, 290, 231, 51))
        font = QtGui.QFont()
        font.setPointSize(19)
        self.swapCurrenciesButton.setFont(font)
        self.swapCurrenciesButton.setObjectName("swapCurrenciesButton")
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
        self.startingCurrencyInputDropDown_2 = QtWidgets.QComboBox(self.centralwidget)
        self.startingCurrencyInputDropDown_2.setGeometry(QtCore.QRect(10, 130, 221, 22))
        self.startingCurrencyInputDropDown_2.setObjectName("startingCurrencyInputDropDown_2")
        self.startingCurrencyInputDropDown_2.addItem("")
        self.startingCurrencyInputDropDown_2.addItem("")
        self.startingCurrencyInputDropDown_2.addItem("")
        self.startingCurrencyInputDropDown_2.addItem("")
        self.startingCurrencyInputDropDown_2.addItem("")
        self.startingCurrencyInputDropDown_2.addItem("")
        self.startingCurrencyInputDropDown_2.addItem("")
        self.startingCurrencyInputDropDown_2.addItem("")
        self.startingCurrencyInputDropDown_2.addItem("")
        self.startingCurrencyInputDropDown_2.addItem("")
        self.startingCurrencyInputDropDown_2.addItem("")
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
        self.startingCurrencyInputDropDown.setItemText(0, _translate("MainWindow", "USD (United States Dollar)"))
        self.startingCurrencyInputDropDown.setItemText(1, _translate("MainWindow", "IDR (Indonesian Rupiah)"))
        self.startingCurrencyInputDropDown.setItemText(2, _translate("MainWindow", "AED (UAE Dirham)"))
        self.startingCurrencyInputDropDown.setItemText(3, _translate("MainWindow", "AUD (Australian Dollar)"))
        self.startingCurrencyInputDropDown.setItemText(4, _translate("MainWindow", "CAD (Canadian Dollar)"))
        self.startingCurrencyInputDropDown.setItemText(5, _translate("MainWindow", "CHF (Swiss Franc)"))
        self.startingCurrencyInputDropDown.setItemText(6, _translate("MainWindow", "EUR (Euro)"))
        self.startingCurrencyInputDropDown.setItemText(7, _translate("MainWindow", "GBP (Pound Sterling)"))
        self.startingCurrencyInputDropDown.setItemText(8, _translate("MainWindow", "HKD (Hong Kong Dollar)"))
        self.startingCurrencyInputDropDown.setItemText(9, _translate("MainWindow", "JPY (Japanese Yen)"))
        self.startingCurrencyInputDropDown.setItemText(10, _translate("MainWindow", "SGD (Singapore Dollar)"))
        self.startingCurrencyInputDropDown_2.setItemText(0, _translate("MainWindow", "USD (United States Dollar)"))
        self.startingCurrencyInputDropDown_2.setItemText(1, _translate("MainWindow", "IDR (Indonesian Rupiah)"))
        self.startingCurrencyInputDropDown_2.setItemText(2, _translate("MainWindow", "AED (UAE Dirham)"))
        self.startingCurrencyInputDropDown_2.setItemText(3, _translate("MainWindow", "AUD (Australian Dollar)"))
        self.startingCurrencyInputDropDown_2.setItemText(4, _translate("MainWindow", "CAD (Canadian Dollar)"))
        self.startingCurrencyInputDropDown_2.setItemText(5, _translate("MainWindow", "CHF (Swiss Franc)"))
        self.startingCurrencyInputDropDown_2.setItemText(6, _translate("MainWindow", "EUR (Euro)"))
        self.startingCurrencyInputDropDown_2.setItemText(7, _translate("MainWindow", "GBP (Pound Sterling)"))
        self.startingCurrencyInputDropDown_2.setItemText(8, _translate("MainWindow", "HKD (Hong Kong Dollar)"))
        self.startingCurrencyInputDropDown_2.setItemText(9, _translate("MainWindow", "JPY (Japanese Yen)"))
        self.startingCurrencyInputDropDown_2.setItemText(10, _translate("MainWindow", "SGD (Singapore Dollar)"))

    #Code related to converting the currency
    def convert_currency_button_pressed(self):
        starting_currency_input = self.startingCurrencyInput.toPlainText()
        
        currency_exchange_value = data['conversion_rates']['IDR']
        print(currency_exchange_value)

        #Exchange currency calculation
        calculate_exchange = float(float(starting_currency_input) / float(currency_exchange_value))
        currency_exchange_output = round(calculate_exchange, 4)
        currency_exchange_output_text = str(currency_exchange_output)

        self.exchangeCurrencyOutput.setText(currency_exchange_output_text)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())