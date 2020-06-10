# flask-course

1. Install Python

2. Install virtualenv
        # apt install virtualenv python3-virtualenv

3. Cria o ambiente virtual
        # virtualenv -p python3 venv    
        
3. Inicializa o ambiente virtual (virtualenv) e instala o flask
        # . venv/bin/activate
        # ./venv/bin/pip3 install flask

4. Verifica o que está instalado no Python
        # pip3 freeze
        # pip3 freeze > requirements.txt

5. Para instalar as versões
        # pip3 install -r requirements.txt

6. Trabalhar com MVC
        # Model
        # View
        # Controller

7. Criar as pastas para a aplicação
        # Model
            # app/models
        # View
            # app/static
            # app/templates
        # Controller
            # app/controllers

8. Criar o arquivo __init__.py
        # Arquivo para trabalhar com módulos, deverá ser criado para a raiz (/app) e para controllers e models
        # cada init indica módulos

9. 