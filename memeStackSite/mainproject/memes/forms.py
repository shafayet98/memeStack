from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired
from flask_wtf.file import FileField, FileAllowed

class MemePostForm(FlaskForm):
    meme_caption = TextAreaField("Meme Caption",validators=[DataRequired()])
    meme_image =  FileField("Update Profile Pictures", validators= [FileAllowed(['jpg','jpeg','png'])])
    submit = SubmitField("Post MEME")