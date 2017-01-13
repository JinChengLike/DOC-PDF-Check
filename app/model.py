from flask_wtf import FlaskForm
from wtforms import SubmitField,FileField
from flask_wtf.file import FileField, FileRequired


class FileCheck(FlaskForm):
    model_file = FileField(validators=[FileRequired('no file')], render_kw={'class': 'sub-btn'})
    check_file = FileField(validators=[FileRequired('no file')], render_kw={'class': 'sub-btn'})
    submit = SubmitField("Submit")

