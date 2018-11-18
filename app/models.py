from app import db

class ApplyAffiliation(db.Model):
    seq = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(100))
    phone = db.Column(db.String(100))
    email = db.Column(db.String(120))
    content = db.Column(db.Text())

    def __repr__(self):
        return '<User {}>'.format(self.name)

