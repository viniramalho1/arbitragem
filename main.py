from app import app, db
from flask import render_template, redirect, request, url_for
from flask_login import login_user, logout_user
from app.models import User, Transacao 


@app.route('/registrar', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        nome = request.form['name']
        cpf = request.form['cpf']

        new_user = User(nome=nome, email=email, senha=pwd, cpf=cpf, saldototal=0)

        db.session.add(new_user)
        db.session.commit()

        return redirect(url_for('login'))

    return render_template('register.html')

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

@app.route('/trocar_senha', methods=['POST', 'GET'])
def trocar_senha():


    return render_template('trocar_senha.html')


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
        email = request.form['email']
        pwd = request.form['password']

        user = User.query.filter_by(email=email).first()

        if user and user.verify_password(pwd):
            login_user(user)
            return redirect(url_for('home'))
        else:
           return redirect(url_for('login'))


    return render_template('login.html')

@app.route('/logout', methods=['POST', 'GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/', methods=['POST', 'GET'])
def home():
    
    return render_template('home.html')

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



app.run(debug=True)

