from PyQt5 import QtCore, QtGui, QtWidgets

import MA_strategy
import yF_Kbar
import RSI_MACD_Strategy
import RSI_MACD_OSC_Strategy
import DI_OSC_SMA
import ADX_MA_RSI
import KD
import MA_KD
import MA_BOLL
import MA_BOLL2
import DI_SMA_RSI_OSC_MACD

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(759, 910)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 440, 141, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(190, 430, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 840, 141, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 30, 621, 381))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("..\\pic\\123.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(190, 490, 81, 41))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 500, 141, 20))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(50, 550, 311, 281))
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setEnabled(True)
        self.radioButton.setGeometry(QtCore.QRect(30, 20, 121, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.radioButton.setFont(font)
        self.radioButton.setCheckable(True)
        self.radioButton.setChecked(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setEnabled(True)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 46, 121, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setEnabled(True)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 73, 171, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setCheckable(True)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setEnabled(True)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 99, 171, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setCheckable(True)
        self.radioButton_4.setObjectName("radioButton_4")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_5.setEnabled(True)
        self.radioButton_5.setGeometry(QtCore.QRect(30, 125, 171, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setCheckable(True)
        self.radioButton_5.setChecked(False)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_6.setEnabled(True)
        self.radioButton_6.setGeometry(QtCore.QRect(30, 151, 181, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setCheckable(True)
        self.radioButton_6.setChecked(False)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_7.setEnabled(True)
        self.radioButton_7.setGeometry(QtCore.QRect(30, 177, 181, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setCheckable(True)
        self.radioButton_7.setChecked(False)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_8.setEnabled(True)
        self.radioButton_8.setGeometry(QtCore.QRect(30, 201, 181, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setCheckable(True)
        self.radioButton_8.setChecked(False)
        self.radioButton_8.setObjectName("radioButton_8")
        self.radioButton_9 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_9.setEnabled(True)
        self.radioButton_9.setGeometry(QtCore.QRect(30, 226, 261, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.radioButton_9.setFont(font)
        self.radioButton_9.setCheckable(True)
        self.radioButton_9.setChecked(False)
        self.radioButton_9.setObjectName("radioButton_9")
        self.radioButton_10 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_10.setEnabled(True)
        self.radioButton_10.setGeometry(QtCore.QRect(30, 250, 271, 21))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(12)
        self.radioButton_10.setFont(font)
        self.radioButton_10.setCheckable(True)
        self.radioButton_10.setChecked(False)
        self.radioButton_10.setObjectName("radioButton_10")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(370, 430, 301, 451))
        font = QtGui.QFont()
        font.setFamily("微軟正黑體")
        font.setPointSize(10)
        self.tableWidget.setFont(font)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "請輸入股票代號"))
        self.pushButton.setText(_translate("MainWindow", "回測"))
        self.label_4.setText(_translate("MainWindow", "回測月數"))
        self.groupBox.setTitle(_translate("MainWindow", "策略選擇"))
        self.radioButton.setText(_translate("MainWindow", "MA交叉"))
        self.radioButton_2.setText(_translate("MainWindow", "RSI + MACD"))
        self.radioButton_3.setText(_translate("MainWindow", "RSI + MACD + OSC"))
        self.radioButton_4.setText(_translate("MainWindow", "DI + OSC + SMA"))
        self.radioButton_5.setText(_translate("MainWindow", "ADX + MA + RSI"))
        self.radioButton_6.setText(_translate("MainWindow", "KD"))
        self.radioButton_7.setText(_translate("MainWindow", "MA + KD"))
        self.radioButton_8.setText(_translate("MainWindow", "MA + BBAND"))
        self.radioButton_9.setText(_translate("MainWindow", "MA + BBAND 2"))
        self.radioButton_10.setText(_translate("MainWindow", "DI + SMA + RSI + OSC + MACD"))

        # 按下button後觸發onClick
        self.pushButton.clicked.connect(self.onClick)

    def onClick(self):
        stock_id = self.lineEdit.text()

        if self.lineEdit_2.text() == 'max':
            period = 'max'
        else:
            period = self.lineEdit_2.text() + "mo"

        if self.radioButton.isChecked():
            df, KPI_df = MA_strategy.main(stock_id, period)
        elif self.radioButton_2.isChecked():
            df, KPI_df = RSI_MACD_Strategy.main(stock_id, period)
        elif self.radioButton_3.isChecked():
            df, KPI_df = RSI_MACD_OSC_Strategy.main(stock_id, period)
        elif self.radioButton_4.isChecked():
            df, KPI_df = DI_OSC_SMA.main(stock_id, period)
        elif self.radioButton_5.isChecked():
            df, KPI_df = ADX_MA_RSI.main(stock_id, period)
        elif self.radioButton_6.isChecked():
            df, KPI_df = KD.main(stock_id, period)
        elif self.radioButton_7.isChecked():
            df, KPI_df = MA_KD.main(stock_id, period)
        elif self.radioButton_8.isChecked():
            df, KPI_df = MA_BOLL.main(stock_id, period)
        elif self.radioButton_9.isChecked():
            df, KPI_df = MA_BOLL2.main(stock_id, period)
        elif self.radioButton_10.isChecked():
            df, KPI_df = DI_SMA_RSI_OSC_MACD.main(stock_id, period)

        yF_Kbar.draw_candle_chart(stock_id, df)
        _translate = QtCore.QCoreApplication.translate

        self.tableWidget.setRowCount(KPI_df.shape[0])
        self.tableWidget.setColumnCount(KPI_df.shape[1])

        self.tableWidget.setVerticalHeaderLabels(KPI_df.index)
        self.tableWidget.setHorizontalHeaderLabels(KPI_df.columns)

        count = 0
        for i in KPI_df['數值']:

            # create table
            item = QtWidgets.QTableWidgetItem()
            self.tableWidget.setItem(count , 0, item)

            # 填入資料
            item = self.tableWidget.item(count, 0)
            item.setText(_translate("MainWindow", str(i)))

            count += 1

        self.label.setPixmap(QtGui.QPixmap("..\\pic\\stock_Kbar.png"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())