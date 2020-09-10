from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from mainproject import db
from mainproject.models import Meme
from mainproject.memes.forms import MemePostForm
from mainproject.memes.picture_handler import add_pic
meme_post = Blueprint('meme_post',__name__)

# create
@meme_post.route('/create',methods = ['GET','POST'])
@login_required
def create_meme():
    form = MemePostForm()
    if form.validate_on_submit():
        getImgModified = add_pic(form.meme_image.data,current_user.username)
        img = form.meme_image.data
        img = img.make_blob()
        print(img)
        meme_post = Meme(meme_caption=form.meme_caption.data,meme_image = img.read(), user_id= current_user.id)
        db.session.add(meme_post)
        db.session.commit()
        flash("Meme Post Created")
        return redirect(url_for('core.index'))
    return render_template('create_meme.html',form = form)