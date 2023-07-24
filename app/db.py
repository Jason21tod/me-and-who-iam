from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class ConversationRegister(db.Model):
    identification = db.Column(db.String, nullable=False, primary_key=True)
    name = db.Column(db.String)


def verify_is_in_db(request_values):
    result = ConversationRegister.query.filter_by(identification=request_values.get('celphone')).first()
    if result == None:
        return False
    return True