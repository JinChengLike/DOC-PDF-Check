#coding=utf-8
from flask_wtf import FlaskForm
from wtforms import SubmitField,FileField,StringField
from flask_wtf.file import FileField, FileRequired,FileAllowed
from wtforms.validators import DataRequired


class FileCheck(FlaskForm):
    model_file = FileField(validators=[FileRequired('no file'), FileAllowed(['pdf', 'doc', 'docx'], 'PDF & Word only!')], render_kw={'class': 'sub-btn'})
    check_file = FileField(validators=[FileRequired('no file'), FileAllowed(['pdf', 'doc', 'docx'], 'PDF & Word only!')], render_kw={'class': 'sub-btn'})
    name = StringField("请输入审核人姓名", validators=[DataRequired()])
    id = StringField("请输入审核人工号", validators=[DataRequired()])
    submit = SubmitField("Submit")

