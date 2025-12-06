# app.py
from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Point(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    waste_type = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "waste_type": self.waste_type
        }

# Serve front-end estático
@app.route("/front")
def front():
    return send_from_directory('.', 'index.html')

# Lista pontos (opcionalmente filtra por ?waste_type=...)
@app.route("/points", methods=["GET"])
def get_points():
    waste = request.args.get("waste_type")
    if waste:
        points = Point.query.filter_by(waste_type=waste).all()
    else:
        points = Point.query.all()
    return jsonify([p.to_dict() for p in points])

# Cadastra ponto
@app.route("/points", methods=["POST"])
def add_point():
    data = request.json
    new_point = Point(
        name=data["name"],
        address=data["address"],
        latitude=float(data["latitude"]),
        longitude=float(data["longitude"]),
        waste_type=data["waste_type"]
    )
    db.session.add(new_point)
    db.session.commit()
    return jsonify(new_point.to_dict()), 201

# Proxy de busca (Nominatim) para evitar CORS e fornecer User-Agent apropriado
@app.route("/search")
def search_address():
    q = request.args.get("q")
    if not q:
        return jsonify([]), 400
    url = "https://nominatim.openstreetmap.org/search"
    try:
        resp = requests.get(
            url,
            params={"format":"json","q":q,"limit":5},
            headers={"User-Agent":"coletaverde/1.0 (matheusgantepenta@gmail.com)"},
            timeout=10
        )
        resp.raise_for_status()
        return jsonify(resp.json())
    except requests.exceptions.RequestException as e:
        # devolve um JSON vazio e código 502 em caso de erro externo
        return jsonify({"error": "geocoding_failed", "details": str(e)}), 502

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
