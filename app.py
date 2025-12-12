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

# LISTAR pontos
@app.route("/points", methods=["GET"])
def get_points():
    waste = request.args.get("waste_type")
    if waste:
        points = Point.query.filter_by(waste_type=waste).all()
    else:
        points = Point.query.all()
    return jsonify([p.to_dict() for p in points])

# ADICIONAR ponto
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

# -----------------------------------------------------------
# NOVA ROTA /search — usando LocationIQ (SEM QUEDAS/403)
# -----------------------------------------------------------
@app.route("/search")
def search_address():
    q = request.args.get("q")
    if not q:
        return jsonify([]), 400

    API_KEY = "pk.02dfdd55b64809e58b2c34ca92859ea6"  # <<< COLOQUE SUA CHAVE AQUI

    url = "https://us1.locationiq.com/v1/search"

    try:
        resp = requests.get(
            url,
            params={
                "key": API_KEY,
                "q": q,
                "format": "json",
                "limit": 5
            },
            timeout=10
        )
        resp.raise_for_status()
        return jsonify(resp.json())

    except requests.exceptions.RequestException as e:
        return jsonify({
            "error": "locationiq_failed",
            "details": str(e)
        }), 502


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
