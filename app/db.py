from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ConversationRegister(db.Model):
    identification = db.Column(db.String, nullable=False, primary_key=True)
    name = db.Column(db.String)
