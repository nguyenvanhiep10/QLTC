import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Database')))
from DBconnect import DBconnect

class giongtc:
    db = DBconnect()
    
    def __init__(self,mag,Loai,Giong,Gia,info):
        self.mag = mag
        self.Loai = Loai
        self.Giong = Giong
        self.Gia = Gia
        self.info = info
        
        
    def them(self):
        sql = "INSERT INTO QLGTC (loai,giong,gia,info) VALUES ('"+str(self.Loai)+"','"+str(self.Giong)+"',"+str(self.Gia)+",'"+str(self.info)+"')"
        giongtc.db.update(sql)
    
    def sua(self):
        sql = "UPDATE QLGTC SET loai='"+str(self.Loai)+"' , giong='"+str(self.Giong)+"',gia="+str(self.Gia)+",info='"+str(self.info)+"' WHERE mag="+str(self.mag)+""
        giongtc.db.update(sql)
        
    def xoa(mag):
        sql = "DELETE FROM QLGTC WHERE mag = "+str(mag)+""
        giongtc.db.update(sql)
    
    def hienthi():
        sql = "SELECT * FROM QLGTC"
        return giongtc.db.hienthi(sql)
    
    def hienthigtl(loai):
        sql = "SELECT giong FROM QLGTC WHERE loai = '"+str(loai)+"'"
        return giongtc.db.hienthi(sql)
    def hienthigia(giong):
        sql = "SELECT gia FROM QLGTC WHERE giong = '"+str(giong)+"'"
        return giongtc.db.hienthi(sql)
    
    def timkiemma(mag):
        sql = "SELECT * FROM QLGTC WHERE mag = "+str(mag)+""
        return giongtc.db.hienthi(sql)
    
    def timkiemgiong(giong):
        sql = "SELECT * FROM QLGTC WHERE giong LIKE '%"+str(giong)+"%';"
        return giongtc.db.hienthi(sql)
    
    

    
    


        

    
    

    
    
    
    
    