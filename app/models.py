from app import db, login_manager, bcrypt
from flask_login import UserMixin

@login_manager.user_loader
def get_user(user_id):
    return User.query.filter_by(id=user_id).first()
# Create a table in the db

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    nome = db.Column(db.String(35), unique=False, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(100), unique=False, nullable=False)
    saldototal = db.Column(db.Float, unique=False, nullable=True)

    def __init__(self, nome, cpf, email, senha, saldototal):
        self.nome = nome
        self.email = email
        self.senha = bcrypt.generate_password_hash(senha)
        self.cpf = cpf
        self.saldototal = saldototal

    def verify_password(self, pwd):
        return bcrypt.check_password_hash(self.senha, pwd)


class Transacao(db.Model):
    idusuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(35), unique=False, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(100), unique=False, nullable=False)

    def __init__(self, nome, cpf, email, senha, saldo_total):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.cpf = cpf

