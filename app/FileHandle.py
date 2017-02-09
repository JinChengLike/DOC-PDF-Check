#coding=utf-8
from app import app
import os
from app import PdfHandle
from app import DocHadnle


class FileHandle():
    def __init__(self,mo,tes):
        self.mo_file = mo
        self.tes_file = tes

    def SaveFile(self):
        if ".pdf" in self.mo_file.filename:
            self.mo_file.save(os.path.join(app.instance_path, 'flies', 'modelfile.pdf'))
            if ".pdf" in self.tes_file.filename:
                self.tes_file.save(os.path.join(app.instance_path, 'flies', 'testfile.pdf'))
                return True
            else:
                return False
        else:
            self.mo_file.save(os.path.join(app.instance_path, 'flies', 'modelfile.doc'))
            if ".doc" or ".docx" in self.tes_file.filename:
                self.tes_file.save(os.path.join(app.instance_path, 'flies', 'testfile.doc'))
                return True
            else:
                return False

    def CheckFile(self):
        if ".pdf" in self.mo_file.filename:
            mo_name = PdfHandle.handle_pdf('instance/flies/modelfile.pdf')
            tes_name = PdfHandle.handle_pdf('instance/flies/testfile.pdf')
            res_mo, res_tes = PdfHandle.Check_PDF(mo_name, tes_name)
            if os.path.exists('instance/flies/modelfile.pdf'):
                 os.remove('instance/flies/modelfile.pdf')
                 os.remove('instance/flies/testfile.pdf')
            return res_mo, res_tes
        else:
            mo_name = DocHadnle.readDocx('instance/flies/modelfile.doc')
            tes_name = DocHadnle.readDocx('instance/flies/testfile.doc')
            res_mo, res_tes = DocHadnle.CheckDoc(mo_name, tes_name)
            if os.path.exists('instance/flies/modelfile.doc'):
                 os.remove('instance/flies/modelfile.doc')
                 os.remove('instance/flies/testfile.doc')
            return res_mo, res_tes
