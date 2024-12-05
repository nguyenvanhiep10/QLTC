import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Database')))
from DBconnect import DBconnect


class nhanvien:
    db = DBconnect()

    def __init__(self, sodt, email, vtri, gt, ca):
        self.sodt = sodt
        self.email = email
        self.vtri = vtri
        self.gt = gt
        self.ca = ca

    def them(self):
        sql = "INSERT INTO QLNV (SDT,Email,VT,GT,Ca) VALUES ('" + str(self.sodt) + "','" + str( self.email) + "','" + str(self.vtri) + "','" + str(self.gt) + "','" + str(self.ca) + "')"
        nhanvien.db.update(sql)

    def sua(self):
        sql = "UPDATE QLNV SET Email ='" + str(self.email) + "',VT = '" + str(str(self.vtri)) + "' , GT = '" + str(self.gt) + "',Ca = '" + str(self.ca) + "' WHERE SDT = '" + str(self.sodt) + "'"
        nhanvien.db.update(sql)

    def xoa(sodt):
        sql = "DELETE FROM QLNV WHERE SDT = '" + str(sodt) + "'"
        nhanvien.db.update(sql)

    def hienthi():
        sql = "SELECT * FROM QLNV"
        return nhanvien.db.hienthi(sql)

    def timkiemsdt(sodt):
        sql = "SELECT * FROM QLNV WHERE SDT LIKE '%" + str(sodt) + "%';"
        return nhanvien.db.hienthi(sql)


















