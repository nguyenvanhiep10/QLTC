import os
import sys
from datetime import datetime
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Database')))
from DBconnect import DBconnect

class dichvu:
    db = DBconnect()
    
    def __init__(self,madv,tkh,sdt,loaitc,tt,ct,pd,ks,thanhtien):
        self.madv = madv
        self.tkh = tkh
        self.sdt = sdt
        self.loaitc = loaitc
        self.tt = tt
        self.ct = ct
        self.pd = pd
        self.ks = ks
        self.thanhtien = thanhtien
        ngay_hien_tai = datetime.now()
        self.ngaydk = ngay_hien_tai.strftime("%Y-%m-%d")
        
        
    def them(self):
        sql = "INSERT INTO QLDV (tkh,sdt,loaitc,tt,ct,pd,ks,thanhtien,ngaydk) VALUES ('"+str(self.tkh)+"','"+str(self.sdt)+"','"+str(self.loaitc)+"','"+str(self.tt)+"','"+str(self.ct)+"','"+str(self.pd)+"','"+str(self.ks)+"',"+str(self.thanhtien)+",'"+str(self.ngaydk)+"')"
        dichvu.db.update(sql)
    
    def sua(self):
        sql = "UPDATE QLDV SET tkh = '"+str(self.tkh)+"', sdt ='"+str(self.sdt)+"', loaitc = '"+str(self.loaitc)+"', tt = '"+str(self.tt)+"' , ct = '"+str(self.ct)+"',pd = '"+str(self.pd)+"',ks = '"+str(self.ks)+"',thanhtien = "+str(self.thanhtien)+", ngaydk = '"+str(self.ngaydk)+"' WHERE madv = "+str(self.madv)+""
        dichvu.db.update(sql)
        
    def xoa(madv):
        sql = "DELETE FROM QLDV WHERE madv = "+str(madv)+""
        dichvu.db.update(sql)
    
    def hienthi():

        sql = """SELECT 
                    madv,
                    tkh,
                    SDT,
                    loaitc,
                    CASE
                        WHEN tt = 'true' AND ct = 'true' THEN 'Trọn gói'
                        WHEN tt = 'true' THEN 'Tắm thơm'
                        WHEN ct = 'true' THEN 'Cắt tỉa lông'
                        ELSE 'Không'
                    END AS dvsp,
                    CASE
                        WHEN pd = 'true' AND ks = 'true' THEN 'Trọn gói'
                        WHEN pd = 'true' THEN 'Phòng dại'
                        WHEN ks = 'true' THEN 'Phòng ký sinh'
                        ELSE 'Không'
                    END AS dvtp,
                    thanhtien,
                    ngaydk

                    FROM QLDV"""
        return dichvu.db.hienthi(sql)
    
    def hienthi1():
        sql = "SELECT * FROM QLDV"
        return dichvu.db.hienthi(sql)
    
    def hienthithongke(nbd,nkt):
        sql = "SELECT * FROM QLDV WHERE ngaydk BETWEEN '"+nbd+"' AND '"+nkt+"'"
        return dichvu.db.hienthi(sql)
    
    
    
    




