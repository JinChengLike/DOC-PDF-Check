#coding=utf-8
from app import app
import os
from flask import render_template
from app import model
from flask_uploads import UploadSet, DOCUMENTS,UploadConfiguration
from app import PdfHandle
from app import DocHadnle
from app import db_model

files_get = UploadSet('files', DOCUMENTS)
UploadConfiguration(app, files_get)


@app.route('/', methods=['GET', 'POST'])
def index():
    form = model.FileCheck()
    if form.validate_on_submit():
        mo_f = form.model_file.data
        che_f = form.check_file.data
        name = form.name.data
        id = form.id.data
        if ".doc" or ".docx" in mo_f.filename:
            mo_f.save(os.path.join(app.instance_path, 'flies', 'modelfile.doc'))
            if ".doc" or ".docx" in che_f.filename:
                che_f.save(os.path.join(app.instance_path, 'flies', 'testfile.doc'))
                mo_name = DocHadnle.readDocx('instance/flies/modelfile.doc')
                tes_name = DocHadnle.readDocx('instance/flies/testfile.doc')
                res = DocHadnle.CheckDoc(mo_name, tes_name)
                db_model.db_insert(id, name, res, che_f.filename)
                return render_template('index.html', form=form, res=res)
            else:
                res = "请上传相同格式文件"
                return render_template('index.html', form=form, res=res)
        if ".pdf" in mo_f.filename:
            mo_f.save(os.path.join(app.instance_path, 'flies', 'modelfile.pdf'))
            if ".pdf" in che_f.filename:
                che_f.save(os.path.join(app.instance_path, 'flies', 'testfile.pdf'))
                mo_name = PdfHandle.handle_pdf('instance/flies/modelfile.pdf')
                tes_name = PdfHandle.handle_pdf('instance/flies/testfile.pdf')
                res = PdfHandle.Check_PDF(mo_name, tes_name)
                db_model.db_insert(id, name, res, che_f.filename)
                return render_template('index.html', form=form, res=res)
            else:
                res = "请上传相同格式文件"
                return render_template('index.html', form=form, res=res)
        else:
            res = "请上传Doc文件或PDF文件"
            return render_template('index.html', form=form, res=res)
    else:
        his = db_model.db_select_history()
        return render_template('index.html', form=form, his=his)


