from data_analysis import db

class RawText(db.Model):

    __tablename__ = "rawtexts"

    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(50), default=None, nullable=False, unique=True)
    text = db.Column(db.Text, default=None, nullable=False)

    def __repr__(self):
        return f"'{self.text}')"
