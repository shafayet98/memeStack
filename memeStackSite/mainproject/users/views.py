from flask import render_template,url_for,flash,redirect,request,Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from mainproject import db
from mainproject.models import User, Meme
from mainproject.users.forms import LoginForm,RegistrationForm,UpdateUserForm
from mainproject.users.picture_handler import add_profile_pic

users = Blueprint('users',__name__)


# logout
@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("core.index"))

# register
@users.route('/register',methods=['GET','POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("Thanks for registration")
        return redirect(url_for("users.login"))
    return render_template('register.html',form= form)

# login
@users.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user.check_password(form.password.data) and user is not None:
            login_user(user)
            flash("Login Success!")
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html',form = form)

# account
# account(update user form)
@users.route('/account',methods=['GET','POST'])
@login_required
def account():
    form = UpdateUserForm()
    if form.validate_on_submit():
        if form.picture.data:
            username = current_user.username
            pic = add_profile_pic(form.picture.data,username)
            current_user.profile_image = pic
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('User Information Updated!')
        return redirect(url_for('users.account'))
    elif request.method == "GET":
        form.username.data = current_user.username
        form.email.data = current_user.email
    profile_image = url_for('static',filename = 'profile_pics/' + current_user.profile_image)
    return render_template('account.html', profile_image = profile_image, form= form)


# user's profile where all post of that w=user can be find.
@users.route('/profile/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first_or_404()
    memes_user = Meme.query.filter_by(author = user).order_by(Meme.date.desc()).all()
    return render_template('profile.html',memes_user= memes_user, user = user)

