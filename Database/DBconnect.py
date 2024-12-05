import sqlite3
import os
from PyQt5 import QtCore, QtGui, QtWidgets

class DBconnect:
    conn = None
    cursor = None
    
    def __init__(self) :
        script_dir = os.path.dirname(os.path.abspath(__file__))
        db_file = os.path.join(script_dir, 'SQLqltc.db')
        self.conn = sqlite3.connect(db_file)
        self.cursor = self.conn.cursor()

    def manhinhtb(self):
        halo=QtWidgets.QMessageBox()
        halo.setInformativeText(f'Cập nhập thành công')
        halo.exec()

    def update(self,sql):
        self.cursor.execute(sql)
        self.conn.commit()
        print("update thanh cong")
        self.manhinhtb()

    def hienthi(self,sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def clconnect(self):
        self.conn.close()
    

