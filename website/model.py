from . import db
from flask_login import UserMixin
class TempatWisata(db.Model):
    __tablename__ = 'tempatWisata'
    Place_Id = db.Column(db.BigInteger, primary_key=True)
    Place_Name = db.Column(db.String(1024), nullable=False)
    Description = db.Column(db.String(1024))
    Category = db.Column(db.String(1024))
    City = db.Column(db.String(1024))
    Price = db.Column(db.BigInteger)
    Rating = db.Column(db.Float)
    Time_Minutes = db.Column(db.String(1024), nullable=True)
    Coordinate = db.Column(db.String(1024))
    Lat = db.Column(db.Float)
    Long = db.Column(db.Float)
    def __repr__(self):
        return f"{{'Place_Id': {self.Place_Id}, 'Place_Name': '{self.Place_Name}', 'Description': '{self.Description}', 'Category': '{self.Category}', 'City': '{self.City}', 'Price': {self.Price}, 'Rating': {self.Rating}, 'Time_Minutes': '{self.Time_Minutes}', 'Coordinate': '{self.Coordinate}', 'Lat': {self.Lat}, 'Long': {self.Long}}}"

class User(UserMixin, db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    Nama_lengkap = db.Column(db.String(60), nullable=False)
    Email = db.Column(db.String(60), nullable=False)
    Password = db.Column(db.String(200), nullable=False)
    Jenis_kelamin = db.Column(db.String(60), nullable=True)
    Tangga_lahir = db.Column(db.String(60), nullable=True)
    def get_id(self):
        return str(self.id)
    def __repr__(self):
        return f"{{'id': {self.id}, 'Nama_lengkap': '{self.Nama_lengkap}', 'Email': '{self.Email}', 'Jenis_kelamin': '{self.Jenis_kelamin}', 'Tangga_lahir': '{self.Tangga_lahir}'}}"
