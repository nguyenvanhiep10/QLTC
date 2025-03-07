# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QLTK.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem 
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'SaveClass')))
from classtk import taikhoan

class Ui_MainWindowtk(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1074, 653)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(440, 0, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 161, 161))
        self.pushButton.setStyleSheet("border-image: url(:/logo/dog.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(240, 50, 641, 16))
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(190, 80, 501, 171))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.tb_tdn = QtWidgets.QLineEdit(self.groupBox)
        self.tb_tdn.setGeometry(QtCore.QRect(170, 40, 311, 31))
        self.tb_tdn.setObjectName("tb_tdn")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.tb_mk = QtWidgets.QLineEdit(self.groupBox)
        self.tb_mk.setGeometry(QtCore.QRect(170, 80, 311, 31))
        self.tb_mk.setObjectName("tb_mk")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 120, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.cb_vt = QtWidgets.QComboBox(self.groupBox)
        self.cb_vt.setGeometry(QtCore.QRect(170, 120, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.cb_vt.setFont(font)
        self.cb_vt.setObjectName("cb_vt")
        self.cb_vt.addItem("")
        self.cb_vt.addItem("")
        self.cb_vt.addItem("")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(570, 340, 481, 201))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox_2)
        self.label_5.setGeometry(QtCore.QRect(10, 50, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tb_tk = QtWidgets.QLineEdit(self.groupBox_2)
        self.tb_tk.setGeometry(QtCore.QRect(160, 50, 281, 31))
        self.tb_tk.setObjectName("tb_tk")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 130, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 260, 541, 321))
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        header = self.tableWidget.horizontalHeader()
        for i in range(self.tableWidget.columnCount()):
            header.setSectionResizeMode(i, QtWidgets.QHeaderView.Stretch)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(920, 0, 151, 141))
        self.pushButton_3.setStyleSheet("border-image: url(:/logo/cool.png);")
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")
        self.bt_t = QtWidgets.QPushButton(self.centralwidget)
        self.bt_t.setGeometry(QtCore.QRect(740, 90, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bt_t.setFont(font)
        self.bt_t.setObjectName("bt_t")
        self.bt_s = QtWidgets.QPushButton(self.centralwidget)
        self.bt_s.setGeometry(QtCore.QRect(740, 170, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bt_s.setFont(font)
        self.bt_s.setObjectName("bt_s")
        self.bt_x = QtWidgets.QPushButton(self.centralwidget)
        self.bt_x.setGeometry(QtCore.QRect(740, 250, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.bt_x.setFont(font)
        self.bt_x.setObjectName("bt_x")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1074, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.hienthi()
        self.bt_t.clicked.connect(lambda:self.them())
        self.bt_s.clicked.connect(lambda:self.sua())
        self.bt_x.clicked.connect(lambda:self.xoa())
        self.pushButton_2.clicked.connect(lambda:self.tk())
        self.tableWidget.cellClicked.connect(lambda:self.cellclick())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Quản Lý Tài Khoản"))
        self.groupBox.setTitle(_translate("MainWindow", "Thêm Tài Khoản"))
        self.label_2.setText(_translate("MainWindow", "Tên đăng nhập:"))
        self.label_3.setText(_translate("MainWindow", "Mật khẩu:"))
        self.label_4.setText(_translate("MainWindow", "Vai trò:"))
        self.cb_vt.setItemText(0, _translate("MainWindow", "Quản lý"))
        self.cb_vt.setItemText(1, _translate("MainWindow", "Nhân viên bán hàng"))
        self.cb_vt.setItemText(2, _translate("MainWindow", "Kế toán"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Tìm Kiếm"))
        self.label_5.setText(_translate("MainWindow", "Tên đăng nhập:"))
        self.pushButton_2.setText(_translate("MainWindow", "Tìm kiếm"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Tên đăng nhập"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Mật khẩu"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Vai trò"))
        self.bt_t.setText(_translate("MainWindow", "Thêm"))
        self.bt_s.setText(_translate("MainWindow", "Sửa"))
        self.bt_x.setText(_translate("MainWindow", "Xóa"))

    def tk(self):
        tk = self.tb_tk.text()
        tc = taikhoan
        py =  tc.timkiemtk(tk)
        self.nhaptable(py)



    def them(self):
        tk = self.tb_tdn.text()
        mk = self.tb_mk.text()
        vt = self.cb_vt.currentText()
        tc = taikhoan(tk, mk, vt)
        tc.them()
        self.hienthi()
    
    
    def sua(self):
        tk = self.tb_tdn.text()
        mk = self.tb_mk.text()
        vt = self.cb_vt.currentText()
        tc = taikhoan(tk, mk, vt)
        tc.sua()
        self.hienthi()
        
    def xoa(self):
        tk = self.tb_tdn.text()
        tc = taikhoan
        tc.xoa(tk)
        self.hienthi()

    def hienthi(self):      
        tk = taikhoan
        data = tk.hienthi()
        self.nhaptable(data)
    
    def nhaptable(self,data):
        self.tableWidget.setRowCount(0)
        for row_data in data:
            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)
            for column_index, cell_data in enumerate(row_data):
                self.tableWidget.setItem(row_position, column_index, QTableWidgetItem(str(cell_data)))

    def cellclick(self):
        row = self.tableWidget.currentRow()
        self.tb_tdn.setText(self.tableWidget.item(row,0).text())
        self.tb_mk.setText(self.tableWidget.item(row,1).text())
        self.cb_vt.setCurrentText(self.tableWidget.item(row,2).text())
import logo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowtk()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
