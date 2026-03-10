from flask import Flask, render_template
from database import db

# models
from models.cliente import Cliente
from models.orcamento import Orcamento
from models.projeto import Projeto

# rotas
from routes.clientes_routes import clientes_bp
from routes.orcamento_routes import orcamentos_bp


app = Flask(__name__)

# configuração do banco
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///marcenaria.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


# registrar rotas (blueprints)
app.register_blueprint(clientes_bp)
app.register_blueprint(orcamentos_bp)

# Página inicial (Dashboard)


@app.route("/")
def home():

    return render_template("index.html")

# Página de projetos


@app.route("/projetos_page")
def pagina_projetos():

    return render_template("projetos.html")

# Criar tabelas automaticamente


with app.app_context():
    db.create_all()

# Rodar servidor

if __name__ == "__main__":
    app.run(debug=True)
