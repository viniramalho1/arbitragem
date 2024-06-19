import requests
import json
from getpass import getpass
import stdiomask

def registrar_usuario():
    nome = input("Digite seu nome:")
    senha = input("Digite seu senha:")
    cpf = input("Digite seu cpf:")
    email = input("Digite seu email:")

    # URL da sua aplicação Flask
    url = 'http://192.168.0.21:5000/registrar'

    # Dados do usuário a serem enviados
    data = {
        "nome": nome,
        "senha": senha,
        "cpf": cpf,
        "email": email
    }

    # Converter os dados para formato JSON
    json_data = json.dumps(data)

    # Definir cabeçalhos para a solicitação
    headers = {'Content-Type': 'application/json'}

    # Enviar solicitação POST
    response = requests.post(url, data=json_data, headers=headers)

    # Verificar a resposta
    if response.status_code == 200:
        print(response.json[message])
    else:
        print("Erro ao registrar usuário:", response.text)

def atualizar_usuario():
    cpf = input("Digite o cpf da conta a ser alterada: ")
    nome = input("Digite seu novo nome: ")
    senha = input("Digite sua nova senha: ")
    novo_cpf = input("Digite seu novo cpf: ")
    email = input("Digite seu novo email: ")
    saldototal = saldo_total(cpf)

    # URL da sua aplicação Flask
    url = 'http://127.0.0.1:5000/atualizar'

    # Dados do usuário a serem enviados
    data = {
        "nome": nome,
        "senha": senha,
        "cpf": cpf,
        "email": email,
        "novo_cpf": novo_cpf,
        "saldototal": saldototal
    }

    # Converter os dados para formato JSON
    json_data = json.dumps(data)

    # Definir cabeçalhos para a solicitação
    headers = {'Content-Type': 'application/json'}

    # Enviar solicitação POST
    response = requests.post(url, data=json_data, headers=headers)

    # Verificar a resposta
    if response.status_code == 200:
        print("Usuário atualizado com sucesso!")
    else:
        print("Erro ao atualizar usuário:", response.text)

def teste():
    valor = input("Digite o valor: ")
    idusuario = input("Digite o id: ")

    # URL da sua aplicação Flask
    url = 'http://192.168.183.128:5000/teste'

    # Dados do usuário a serem enviados
    data = {
        "valor": valor,
        "idusuario": idusuario
    }

    # Converter os dados para formato JSON
    json_data = json.dumps(data)

    # Definir cabeçalhos para a solicitação
    headers = {'Content-Type': 'application/json'}

    # Enviar solicitação POST
    response = requests.post(url, data=json_data, headers=headers)

    # Verificar a resposta
    if response.status_code == 200:
        print(response.json()['message'])
    else:
        print("Erro ao atualizar usuário:", response.text)

def remover_usuario():
    cpf = input("Digite o cpf da conta a ser removida: ")

    # URL da sua aplicação Flask
    url = 'http://127.0.0.1:5000/remover'

    # Dados do usuário a serem enviados
    data = {
        "cpf": cpf
    }

    # Converter os dados para formato JSON
    json_data = json.dumps(data)

    # Definir cabeçalhos para a solicitação
    headers = {'Content-Type': 'application/json'}

    # Enviar solicitação POST
    response = requests.post(url, data=json_data, headers=headers)

    # Verificar a resposta
    if response.status_code == 200:
        print("Usuário removido com sucesso!")
    else:
        print("Erro ao remover usuário:", response.text)

def pagina_principal():
    cpf = input("Digite seu cpf: ")
    print(saldo_total(cpf))

def saldo_total(cpf):
    # URL da sua aplicação Flask
    url = 'http://192.168.0.21:5000/saldo_total'

    # Dados do usuário a serem enviados
    data = {
        "cpf": cpf
    }

    # Converter os dados para formato JSON
    json_data = json.dumps(data)

    # Definir cabeçalhos para a solicitação
    headers = {'Content-Type': 'application/json'}

    # Enviar solicitação POST
    response = requests.post(url, data=json_data, headers=headers)

    # Verificando se a requisição foi bem-sucedida (status code 200)
    if response.status_code == 200:
        # Extraindo os dados da resposta (em formato JSON, por exemplo)
        response_data = response.json()
        return(response_data['message'])
    else:
        print("Erro:", response.status_code)

def login():
    email = input("Digite seu email: ")
    senha = stdiomask.getpass(prompt="Digite seu senha: ", mask='*')

    # URL da sua aplicação Flask
    url = 'http://127.0.0.1:5000/login'

    # Dados do usuário a serem enviados
    data = {
        "email": email,
        "senha": senha,
    }

    # Converter os dados para formato JSON
    json_data = json.dumps(data)

    # Definir cabeçalhos para a solicitação
    headers = {'Content-Type': 'application/json'}

    # Enviar solicitação POST
    response = requests.post(url, data=json_data, headers=headers)

    # Verificar a resposta
    if response.status_code == 200:
    # Analisar a resposta JSON
        response_data = response.json()
        # Se não houver erro, exibir mensagem de sucesso
        print(response_data['message'])

    else:
        # Se a resposta não for 200, exibir mensagem de erro
        print("Erro:", response.status_code)

def adicionar_saldo():
    valor = input("Quanto quer adicionar?")
    idusuario = input("ID do usuario:")

    # URL da sua aplicação Flask
    url = 'http://127.0.0.1:5000/adicionar_saldo'

    # Dados do usuário a serem enviados
    data = {
        "valor": valor,
        "idusuario": idusuario,
    }

    # Converter os dados para formato JSON
    json_data = json.dumps(data)

    # Definir cabeçalhos para a solicitação
    headers = {'Content-Type': 'application/json'}

    # Enviar solicitação POST
    response = requests.post(url, data=json_data, headers=headers)

    # Verificando se a requisição foi bem-sucedida (status code 200)
    if response.status_code == 200:
        # Extraindo os dados da resposta (em formato JSON, por exemplo)
        response_data = response.json()
        print(response_data['message'])
    else:
        print("Erro:", response.status_code)

def rendimento_diario():
    # URL da sua aplicação Flask
    cpf = input("Digite seu CPF")
    saldo = saldo_total(cpf)
    print(f'''Saldo = {saldo}
    Saldo futuro(1 dia) = {saldo * 1.01}
    Saldo futuro(30 dias) = {saldo * 1.30}
    Saldo futuro(anual) = {saldo * 3.65}''')

def menu():
    print("Menu:")
    print("[1] Registrar Usuário")
    print("[2] Fazer Login")
    print("[3] Atualizar Usuário")
    print("[4] Deletar Usuário")
    print("[5] Pagina Principal")
    print("[6] Fazer Investimento")
    print("[7] Página de Rendimento Diário")
    print("[8] Adicionar saldo")
    print("[0] Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        registrar_usuario()
    elif opcao == '2':
        login()
        pass
    elif opcao == '3':
        atualizar_usuario()
    elif opcao == '4':
        remover_usuario()
        pass
    elif opcao == '5':
        pagina_principal()
        pass
    elif opcao == '6':
        teste()
        pass
    elif opcao == '7':
        rendimento_diario()
        pass
    elif opcao == '8':
        adicionar_saldo()
        pass
    elif opcao == '0':
        print("Saindo do programa...")
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    while True:
        menu()