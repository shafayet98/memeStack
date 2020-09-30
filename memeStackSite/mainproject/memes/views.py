from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from mainproject import db
from mainproject.models import Meme, User
from mainproject.memes.forms import MemePostForm
from mainproject.memes.picture_handler import add_pic
meme_post = Blueprint('meme_post',__name__)

# create
@meme_post.route('/create',methods = ['GET','POST'])
@login_required
def create_meme():
    form = MemePostForm()
    if form.validate_on_submit():
        # isuploadable = canUpload(form.meme_image.data,current_user.username)
        getImgModified = add_pic(form.meme_image.data,current_user.username)
        if getImgModified != "False":
            meme_post = Meme(meme_caption=form.meme_caption.data,meme_image = getImgModified, user_id= current_user.id)
            db.session.add(meme_post)
            db.session.commit()
            flash("Meme Post Created")
            return redirect(url_for('core.index'))
        else:
            flash("Machine detected that the image you upload is not a meme. Next time please upload a valid picture.")
    return render_template('create_meme.html',form = form)

# show
@meme_post.route('/<int:meme_post_id>')
def meme(meme_post_id):
    each_meme = Meme.query.get_or_404(meme_post_id)
    user = User.query.filter_by(id = each_meme.user_id).first_or_404()
    return render_template('meme_show.html',post = each_meme,user = user)

# delete
@meme_post.route('/<int:meme_post_id>/delete',methods = ['GET','POST'])
@login_required
def delete_meme(meme_post_id):
    del_meme = Meme.query.get_or_404(meme_post_id)
    if del_meme.author != current_user:
        abort(403)
    db.session.delete(del_meme)
    db.session.commit()
    flash("Blog Post Deleted")
    return redirect(url_for('users.profile',username= current_user.username))