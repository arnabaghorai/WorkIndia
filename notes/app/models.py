from app import db, ma

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(100))

    def __repr__(self):
        return f"<User {self.username}>"

class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    note = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer)

class NoteSchema(ma.Schema):

    class Meta:
        fields = ('id','note')

note_schema = NoteSchema()
notes_schema = NoteSchema(many=True)