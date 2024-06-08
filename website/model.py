from .config import app
import flask_sqlalchemy as sqlalchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/users'
db = sqlalchemy.SQLAlchemy(app)

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

