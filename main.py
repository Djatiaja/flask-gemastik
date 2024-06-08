from website.config import app
from website.model import db, TempatWisata
from website import machine

@app.route('/tempat_wisata/<int:tempat_wisata_id>')
def get_tempat_wisata(tempat_wisata_id):
    tempat_wisata = TempatWisata.query.filter_by(Place_Id=tempat_wisata_id).first()
    return tempat_wisata.__repr__()

@app.route('/get_recommendation/<int:tempat_wisata_id>')
def get_recommendation(tempat_wisata_id):
    data= machine.get_recommendation(tempat_wisata_id)
    return data

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)