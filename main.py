from flask import Flask

app = Flask(__name__)

# Importa a lógica da tela principal
from view.tela_principal import tela_principal_blueprint

# Registra o blueprint da tela principal
app.register_blueprint(tela_principal_blueprint)

if __name__ == '__main__':
    app.run()