from flask import Flask, jsonify, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configuração do banco de dados SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo de dados para os pontos de coleta
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

@app.route("/")
def home():
    return "Aplicação Coleta Verde com banco de dados!"

# -------------------------------
# Rotas de pontos de coleta
# -------------------------------
@app.route("/points", methods=["GET"])
def get_points():
    points = Point.query.all()
    return jsonify([p.to_dict() for p in points])

@app.route("/points", methods=["POST"])
def add_point():
    data = request.json
    new_point = Point(
        name=data["name"],
        address=data["address"],
        latitude=data["latitude"],
        longitude=data["longitude"],
        waste_type=data["waste_type"]
    )
    db.session.add(new_point)
    db.session.commit()
    return jsonify(new_point.to_dict()), 201

# -------------------------------
# Rota para exibir o front-end
# -------------------------------
@app.route("/front")
def front():
    return send_from_directory('.', 'index.html')

# -------------------------------
# Inicialização da aplicação
# -------------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
