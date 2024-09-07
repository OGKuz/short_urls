from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class NewShortUrl(FlaskForm):

    long_url = StringField('long_url', validators=[DataRequired(), Length(max = 255)])
    sub_button = SubmitField('Get_short_url')