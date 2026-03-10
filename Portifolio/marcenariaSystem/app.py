from flask import Flask, render_template
from database import db

from models.cliente import Cliente
from models.orcamento import Orcamento
from models.projeto import Projeto

from routes.clientes_routes import clientes_bp
from routes.orcamento_routes import orcamentos_bp
from routes.projetos_routes import projetos_bp

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///marcenaria.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

app.register_blueprint(clientes_bp)
app.register_blueprint(orcamentos_bp)
app.register_blueprint(projetos_bp)


@app.route("/")
def home():

    total_clientes = Cliente.query.count()

    total_orcamentos = Orcamento.query.count()

    projetos_producao = Projeto.query.filter_by(status="Em produção").count()

    projetos_finalizados = Projeto.query.filter_by(status="Finalizado").count()

    projetos_recentes = Projeto.query.order_by(Projeto.id.desc()).limit(5)

    return render_template(
        "index.html",
        total_clientes=total_clientes,
        total_orcamentos=total_orcamentos,
        projetos_producao=projetos_producao,
        projetos_finalizados=projetos_finalizados,
        projetos_recentes=projetos_recentes
    )


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
