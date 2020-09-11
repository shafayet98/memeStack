from mainproject import db, login_manager
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


# create models 

class User(db.Model,UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key= True)
    profile_image = db.Column(db.String(20),nullable=False,default='default_profile.png')
    email = db.Column(db.String(64),unique = True, index = True)
    username = db.Column(db.String(64),unique = True, index = True)
    password_hash = db.Column(db.String(128))

    memes = db.relationship('Meme',backref='author',lazy = True)

    def __init__(self, email, username, password):
         self.email = email
         self.username = username
         self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f"Username: {self.username}"

class Meme(db.Model):
    users = db.relationship(User)
    id = db.Column(db.Integer,primary_key= True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable = False)
    date = db.Column(db.DateTime,nullable=False, default = datetime.utcnow)
    meme_caption = db.Column(db.Text,nullable = False)
    meme_image = db.Column(db.String(128),nullable=False)
    

    def __init__(self, meme_caption, meme_image, user_id):
        self.meme_caption = meme_caption
        self.meme_image = meme_image
        self.user_id = user_id

    def __repr__(self):
        return f"post_id: {self.id}"


