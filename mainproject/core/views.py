from flask import render_template,request,Blueprint
from mainproject.models import Meme

core = Blueprint('core',__name__)

@core.route('/')
def index():
    all_memes = Meme.query.filter_by(user_id = 1).first()
    return render_template("index.html",meme_img = all_memes.meme_image)

@core.route('/about')
def about():
    return render_template('about.html')