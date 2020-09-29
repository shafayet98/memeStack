import os
from PIL import Image
from flask import url_for, current_app
import datetime
import numpy as np
import io
import tensorflow
from tensorflow import Graph
from tensorflow import keras as keras_lib
from tensorflow.keras import backend as K
from tensorflow.keras.preprocessing import image
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from tensorflow.python.keras.models import load_model



global CATEGORIES
global model
CATEGORIES = ['Not Meme', 'Meme']

def add_pic(pic_upload, username):
    filename = pic_upload.filename
    ext_type = filename.split('.')[-1]
    strorage_filename = str(username)+str(datetime.datetime.now().time())+"."+ "png"
    filepath = os.path.join(current_app.root_path,'static/memes',strorage_filename)

    # outputsize = (200,200)
    pic = Image.open(pic_upload)
    # pic.thumbnail(outputsize)
    pic.save(filepath)

    model = load_model('mainproject/memes/model.v1.h5')
    img = image.load_img(filepath, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    prediction = model.predict(x)
    class_lable = CATEGORIES[int(prediction[0][0])]

    if class_lable == "Meme":
        return strorage_filename
    else:
        os.remove(filepath)
        return "False"



