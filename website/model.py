from . import db
from flask_login import UserMixin
class TempatWisata(db.Model):
    __tablename__ = 'tempatwisata'
    
    Place_Name = db.Column(db.String(512), nullable=False)
    Description = db.Column(db.String(512), nullable=False)
    Category = db.Column(db.String(512), nullable=False)
    City = db.Column(db.String(512), nullable=False)
    Price = db.Column(db.Integer, nullable=False)
    Rating = db.Column(db.Float, nullable=False)
    Time_Minutes = db.Column(db.String(512), nullable=False)
    Lat = db.Column(db.Float, nullable=False)
    Long = db.Column(db.Float, nullable=False)
    Place_Id = db.Column(db.Integer, primary_key=True, nullable=False)
    Image = db.Column(db.String(512), nullable=False)
    def __repr__(self):
        return f"{{'Place_Name': '{self.Place_Name}', 'Description': '{self.Description}', 'Category': '{self.Category}', 'City': '{self.City}', 'Price': {self.Price}, 'Rating': {self.Rating}, 'Time_Minutes': '{self.Time_Minutes}', 'Lat': {self.Lat}, 'Long': {self.Long}, 'Place_Id': {self.Place_Id}, 'Image': '{self.Image}'}}"

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
