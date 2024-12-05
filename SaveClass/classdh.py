import os
import sys
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Database')))
from DBconnect import DBconnect

class donhang:
    db = DBconnect()
    
    def __init__(self,matc,cccd,ht,sdt):     
        self.matc = matc
        self.cccd = cccd
        self.ht = ht
        self.sdt = sdt
        ngay_hien_tai = datetime.now()
        self.ngayban = ngay_hien_tai.strftime("%Y-%m-%d")
        
        
    def them(self):
        sql = "INSERT INTO QLDH (matc,CCCD,ht,SDT,ngayban) VALUES ("+str(self.matc)+",'"+str(self.cccd)+"','"+str(self.ht)+"','"+str(self.sdt)+"','"+str(self.ngayban)+"')"
        donhang.db.update(sql)
        
    
    def hienthi(ngayt,ngayd):
        sql = "SELECT madh,QLDH.matc,CCCD,ht,SDT,ngayban,QLTC.gia as tongtien FROM QLDH INNER JOIN QLTC ON QLTC.matc = QLDH.matc WHERE QLTC.giong = 'Chó' AND  ngayban BETWEEN '"+ngayt+"' AND '"+ngayd+"' "
        return donhang.db.hienthi(sql)

    


       


    
    

    
    


        

    
    

    
    
    
    
    