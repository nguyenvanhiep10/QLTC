import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Database')))
from DBconnect import DBconnect

class taikhoan:
    db = DBconnect()
    
    def __init__(self,tk,mk,vt):
        self.tk = tk
        self.mk = mk
        self.vt = vt
        
        
    def them(self):
        sql = "INSERT INTO QLTk (TK,MK,VT) VALUES ('"+str(self.tk)+"','"+str(self.mk)+"','"+str(self.vt)+"')"
        taikhoan.db.update(sql)
    
    def sua(self):
        sql = "UPDATE QLTK SET MK = '"+str(self.mk)+"', VT ='"+str(self.vt)+"' WHERE TK = '"+str(self.tk)+"'"
        taikhoan.db.update(sql)
        
    def xoa(tk):
        sql = "DELETE FROM QLTK WHERE TK = '"+str(tk)+"'"
        taikhoan.db.update(sql)
    
    def hienthi():
        sql = "SELECT * FROM QLTK"
        return taikhoan.db.hienthi(sql)
    
    
    def timkiemtk(tdn):
        sql = "SELECT * FROM QLTK WHERE TK LIKE '%"+str(tdn)+"%';"
        return taikhoan.db.hienthi(sql)
    
    def dmk(self):
        sql = "UPDATE QLTK SET MK = '"+str(self.mk)+"'WHERE TK = '"+str(self.tk)+"'"
        taikhoan.db.update(sql)
    def gettk(tk):
        sql = "SELECT * FROM QLTK WHERE TK = '"+str(tk)+"';"
        return taikhoan.db.hienthi(sql)
    
    
    

    
    


        

    
    

    
    
    
    
    