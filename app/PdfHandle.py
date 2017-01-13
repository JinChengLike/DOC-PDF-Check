#coding=utf-8
from pdfminer.converter import PDFPageAggregator
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfpage import PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.layout import *
import re
import sys


reload(sys)
sys.setdefaultencoding("utf-8")
#CODEC = 'utf-8'


def handle_pdf(fliename):
    a = []
    fp = open(fliename)
    parser = PDFParser(fp)
    document = PDFDocument(parser)
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    rsrcmgr = PDFResourceManager(caching=False)
    laparams = LAParams()
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    replace = re.compile(r'\s+');
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        layout = device.get_result()
        for x in layout:
            if (isinstance(x, LTTextBoxHorizontal)):
                text = re.sub(replace, '', x.get_text())
                if len(text) != 0:
                    a.append(text)
    return a


def Check_PDF(mo_name, tes_name):
    mo_file = mo_name
    tes_file = tes_name
    len_1 = len(mo_name)
    len_2 = len(tes_name)
    codemessage = ""
    if len_1 != len_2:
        codemessage = "文件长度不同，请检查"
    i =0
    while(i <= len_1):
        try:
            if mo_file[i] != tes_file[i]:
                codemessage = "模版为"+mo_file[i]+",实际为"+tes_file[i]
                break
            else:
                i += 1
        except IndexError:
            continue
        if i == len_1:
            break
    if "模版为" and "实际为" not in codemessage:
        codemessage = "文件无错误"
    return codemessage


# if __name__ == '__main__':
#
#     mo_name = handle_pdf('../instance/flies/modelfile.pdf')
#     tes_name = handle_pdf('../instance/flies/testfile.pdf')
#     aaa = Check_PDF(mo_name, tes_name)