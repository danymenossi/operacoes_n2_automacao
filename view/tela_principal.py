from flask import Blueprint, render_template, request

# Cria o blueprint para a tela principal
tela_principal_blueprint = Blueprint('tela_principal', __name__)

# Define a rota para a tela principal
@tela_principal_blueprint.route('/')
def tela_principal():
    return render_template('saudacao.html')

# Define a rota para o processamento do formulário
@tela_principal_blueprint.route('/saudacao', methods=['POST'])
def saudacao():
    nome = request.form['nome']
    return f'Olá, {nome}! Bem-vindo(a) à nossa aplicação web!'