#coding=utf-8
from app import app
from flask import render_template
from app import model
from flask_uploads import UploadSet, DOCUMENTS,UploadConfiguration
from app import db_model
from FileHandle import FileHandle

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
        f = FileHandle(mo_f, che_f)
        save_res = f.SaveFile()
        if not save_res:
            res = "请上传相同格式文件"
            return render_template('index.html', form=form, res_mo=res, res_tes=res)
        elif save_res:
            res_mo, res_tes = f.CheckFile()
            db_model.db_insert(id, name, res_mo, res_tes, che_f.filename)
            return render_template('index.html', form=form, res_mo=res_mo, res_tes=res_tes)
    else:
        his = db_model.db_select_history()
        return render_template('index.html', form=form, his=his)


