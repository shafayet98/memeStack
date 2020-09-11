from flask import render_template,request,Blueprint
from mainproject.models import Meme

core = Blueprint('core',__name__)

@core.route('/')
def index():
    # all_memes = Meme.query.filter_by(user_id = 1).first()
    memes = Meme.query.order_by(Meme.date.desc()).all()
    return render_template("index.html",memes = memes)

@core.route('/about')
def about():
    return render_template('about.html')