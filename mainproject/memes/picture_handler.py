import os
from PIL import Image
from flask import url_for, current_app
import datetime



def add_pic(pic_upload, username):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    strorage_filename = str(username)+str(datetime.datetime.now().time())+"."+ ext_type
    filepath = os.path.join(current_app.root_path,'static/memes',strorage_filename)

    outputsize = (200,200)
    pic = Image.open(pic_upload)
    pic.thumbnail(outputsize)
    pic.save(filepath)

    return strorage_filename