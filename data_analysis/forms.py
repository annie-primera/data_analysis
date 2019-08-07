from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms.validators import DataRequired, ValidationError
from wtforms import SubmitField
from data_analysis.models import RawText


class TextUpload(FlaskForm):
    text = FileField('Upload Text', validators=[FileAllowed(['txt']), DataRequired()])
    submit = SubmitField('Upload')

    def validate_username(self, filename):
        if filename == RawText.query.filter_by(filename=filename).first():
                raise ValidationError('That file has already been uploaded.')
