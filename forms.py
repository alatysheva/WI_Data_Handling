from flask_wtf import FlaskForm
from wtforms import StringField, FileField, validators, SubmitField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional

from classes import Configuration


class UploadForm(FlaskForm):
    filename = StringField('Enter', [validators.DataRequired()])
    filetype = SelectField("File Type ", choices=[
        ("las", "las"),
        ("csv", "csv"),
        ('dlis', 'dlis'),
    ('xml', 'xml')])
    servicecompany = StringField('Enter', [validators.DataRequired()])
    BU = StringField('Enter', [validators.DataRequired()])
    asset = StringField('Enter', [validators.DataRequired()])
    wellname = StringField('Enter', validators=[InputRequired()])
    file = FileField()
    # representation of data points for equal depths
    represent = SelectField("File Type ", choices=[
        ("Minimum value", "Minimum value"),
        ("Maximum value", "Maximum value"),
        ('Average value', 'Average value')])


class VisualizeCsvForm(FlaskForm):
    columns = StringField('columns', render_kw={'placeholder': 'Optional'}, validators=[Optional()])
    start = StringField('start', [validators.DataRequired()])
    measure = StringField('measure', [validators.DataRequired()])


class DLISForm(FlaskForm):
    frameNumber = SelectField('Frame', choices=[], coerce=int)
    visual1 = SubmitField('Visualize')


class Credentials(FlaskForm):
    uidwell = StringField('uidwell', [validators.DataRequired()])
    uidwellbore = StringField('uidwellbore', [validators.DataRequired()])
    runid = StringField('runid', [validators.DataRequired()])
    uidwi = StringField('uiwdi', [validators.DataRequired()])
    purpose1 = StringField('purpose1', [validators.DataRequired()])
    ser, choices1 = Configuration().serviceTypeOptionsforXML()
    servicetype = SelectField("Service Type ", choices=choices1)
    ser1, choices1 = Configuration().dataTypeOptions()
    datatype = SelectField("Data Type ", choices=choices1)
    uid = BooleanField('uid')


class Credentials1(FlaskForm):
    uidwell = StringField('uidwell', [validators.DataRequired()])
    uidwellbore = StringField('uidwellbore', [validators.DataRequired()])
    runid = StringField('runid', [validators.DataRequired()])
    uidwi = StringField('uiwdi', [validators.DataRequired()])
    purpose1 = StringField('purpose1', [validators.DataRequired()])
    ser, choices1 = Configuration().serviceTypeOptionsforXML()
    servicetype = SelectField("Service Type ", choices=choices1)
    ser1, choices1 = Configuration().dataTypeOptions()
    datatype = SelectField("Data Type ", choices=choices1)
    uid = BooleanField('uid')
    frameNumber = SelectField('Frame', choices=[], coerce=int)