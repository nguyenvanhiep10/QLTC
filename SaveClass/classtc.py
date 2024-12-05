import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Database')))
from DBconnect import DBconnect

class thucung:
    db = DBconnect()
    
    def __init__(self,matc,tuoi,loai,gt,giong,gia,tp):
        self.matc = matc
        self.tuoi = tuoi
        self.loai = loai
        self.gt = gt
        self.giong = giong
        self.gia = gia
        self.tp = tp
        
        
    def them(self):
        sql = "INSERT INTO QLTC (tuoi,loai,gt,giong,gia,tp) VALUES ("+str(self.tuoi)+",'"+str(self.loai)+"','"+str(self.gt)+"','"+str(self.giong)+"',"+str(self.gia)+",'"+str(self.tp)+"')"
        thucung.db.update(sql)
    
    def sua(self):
        sql = "UPDATE QLTC SET tuoi = "+str(self.tuoi)+", loai ='"+str(self.loai)+"',gt = '"+str(str(self.gt))+"' , giong = '"+str(self.giong)+"',gia = "+str(self.gia)+", tp = '"+str(self.tp)+"' WHERE matc = "+str(self.matc)+""
        thucung.db.update(sql)
        
    def xoa(matc):
        sql = "DELETE FROM QLTC WHERE matc = "+str(matc)+""
        thucung.db.update(sql)
    
    def hienthi():
        sql = "SELECT * FROM QLTC"
        return thucung.db.hienthi(sql)
    
    def timkiemma(matc):
        sql = "SELECT * FROM QLTC WHERE matc = "+str(matc)+""
        return thucung.db.hienthi(sql)
    
    def timkiemgiong(giong):
        sql = "SELECT * FROM QLTC WHERE giong LIKE '%"+str(giong)+"%';"
        return thucung.db.hienthi(sql)
    
    def timkiemnc(loai,giong,tuoi,tp,gt,giat,giad):
        if (giat == "" and giad == ""):
            sql = "SELECT * FROM QLTC WHERE loai LIKE '%"+str(loai)+"%' AND giong LIKE '%"+str(giong)+"%' AND tuoi like '%"+str(tuoi)+"%' AND tp like '%"+str(tp)+"%' AND gt like '%"+str(gt)+"%'"
        elif (giat == "" and giad != ""):
            sql = "SELECT * FROM QLTC WHERE loai LIKE '%"+str(loai)+"%' AND giong LIKE '%"+str(giong)+"%' AND tuoi like '%"+str(tuoi)+"%' AND tp like '%"+str(tp)+"%' AND gt like '%"+str(gt)+"%' AND gia <= "+str(giad)+""           
        elif (giat != "" and giad == ""):
            sql = "SELECT * FROM QLTC WHERE loai LIKE '%"+str(loai)+"%' AND giong LIKE '%"+str(giong)+"%' AND tuoi like '%"+str(tuoi)+"%' AND tp like '%"+str(tp)+"%' AND gt like '%"+str(gt)+"%' AND gia >= "+str(giat)+""
        else:
             sql = "SELECT * FROM QLTC WHERE loai LIKE '%"+str(loai)+"%' AND giong LIKE '%"+str(giong)+"%' AND tuoi like '%"+str(tuoi)+"%' AND tp like '%"+str(tp)+"%' AND gt like '%"+str(gt)+"%' AND gia >= "+str(giat)+" AND gia <= "+str(giad)+""
        return thucung.db.hienthi(sql)   


    
    

    
    


        

    
    

    
    
    
    
    