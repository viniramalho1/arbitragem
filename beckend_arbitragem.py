from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost:3306/arbitragem'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

class User(db.Model):
    idusuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(35), unique=False, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(100), unique=False, nullable=False)
    saldototal = db.Column(db.Float, unique=False, nullable=True)

class Transacao(db.Model):
    idusuario = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(35), unique=False, nullable=False)
    cpf = db.Column(db.String(11), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    senha = db.Column(db.String(100), unique=False, nullable=False)

@app.route('/registrar', methods=['POST'])
def register():
    data = request.get_json()

    hashed_password = bcrypt.generate_password_hash(data['senha']).decode('utf-8')
    new_user = User(nome=data['nome'], email=data['email'], senha=hashed_password, cpf=data['cpf'], saldototal=0)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Usuario Resgistrado com Sucesso!'})

@app.route('/atualizar', methods=['POST'])
def atualizar_usuario():
    data = request.get_json()

    hashed_password = bcrypt.generate_password_hash(data['senha']).decode('utf-8')

    user = User.query.filter_by(cpf=data['cpf']).first()

    user.nome = data['nome']
    user.email = data['email']
    user.senha = hashed_password
    user.cpf = data['novo_cpf']
    user.saldototal = data['saldototal']

    db.session.commit()

    return jsonify({'message': 'Usuario Atualizado com Sucesso!'})

@app.route('/remover', methods=['POST'])
def remover_usuario():
    data = request.get_json()

    user = User.query.filter_by(cpf=data['cpf']).first()

    db.session.delete(user)  # Remove o usuário do banco de dados
    db.session.commit()

    return jsonify({'message': 'Usuario Removido com Sucesso!'})

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.get_json()

        # email = request.form['email']
        # senha = request.form['password']

        email = data['email']
        senha = data['senha']
        
        user = User.query.filter_by(email=email).first()
        
        if user and bcrypt.check_password_hash(user.senha, senha):
            # Login successful
            return jsonify({'message': 'Login efetudo com Sucesso!'})
            # return redirect(url_for('index'))  # Redirecionar para a página principal após o login
        else:
            # Login failed
            return jsonify({'message': 'Usuario ou Senha estão incorretos!'})
            # return render_template('login.html', error='Credenciais inválidas. Por favor, tente novamente.')
    
    return render_template('login.html')

@app.route('/saldo_total', methods=['POST'])
def saldo_total():
    data = request.get_json()

    # Recuperar o saldo do usuário
    usuario = User.query.filter_by(cpf=data['cpf']).first()  # Substitua "Nome do Usuário" pelo nome do usuário atual
    saldo = usuario.saldototal

    return jsonify({'message': f'{saldo}'})
    # Renderizar o template com o saldo do usuário
    # return render_template('index.html', saldo=saldo)

@app.route('/adicionar_saldo', methods=['POST'])
def adicionar_saldo():

    data = request.get_json()

    valor = data['valor']
    idusuario = data['idusuario']

    # Recuperar o saldo do usuário
    user = User.query.filter_by(idusuario=idusuario).first()  # Substitua "Nome do Usuário" pelo nome do usuário atual
    saldo = user.saldototal

    saldo_total = saldo + float(valor)

    user.saldototal = saldo_total

    db.session.commit()

    return jsonify({'message': f'R$ {float(valor)} adicionado com sucesso!'})

@app.route('/rendimento', methods=['GET'])
def rendimento_diario():
    # Recuperar o saldo do usuário
    usuario = User.query.filter_by(cpf="5").first()  # Substitua "Nome do Usuário" pelo nome do usuário atual
    saldo = usuario.saldototal

    return jsonify({'message': f'''Saldo = {saldo}
    Saldo futuro(1 dia) = {saldo * 1.01}
    Saldo futuro(30 dias) = {saldo * 1.30}
    Saldo futuro(anual) = {saldo * 3.65}'''})
    # Renderizar o template com o saldo do usuário
    # return render_template('index.html', saldo=saldo)

@app.route('/investir', methods=['POST'])
def investir():
    
    data = request.get_json()

    valor = data['valor']
    idusuario = data['idusuario']

    # Recuperar o saldo do usuário
    user = User.query.filter_by(idusuario=idusuario).first()  # Substitua "Nome do Usuário" pelo nome do usuário atual
    saldo = user.saldototal

    saldo_total = saldo + float(valor)

    user.saldototal = saldo_total

    db.session.commit()

    return jsonify({'message': f'R$ {float(valor)} adicionado com sucesso!'})

@app.route('/', methods=['POST', 'GET'])
def home():

    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
