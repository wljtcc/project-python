# flask-course

        https://flask.palletsprojects.com/en/1.1.x/installation/

1. Install Python

2. Install virtualenv

        # apt install virtualenv python3-virtualenv

3. Cria o ambiente virtual

        # virtualenv -p python3 venv    
        
3. Inicializa o ambiente virtual (virtualenv) e instala o flask

        # . venv/bin/activate
        # ./venv/bin/pip3 install flask

4. Install Flask Environment

        venv/bin/pip3 install python-dotenv

5. Verifica o que está instalado no Python

        # pip3 freeze
        # pip3 freeze > requirements.txt

6. Para instalar as versões

        # pip3 install -r requirements.txt

7. Trabalhar com MVC

        # Model
        # View
        # Controller

8. Criar as pastas para a aplicação

        # Model
            # app/models
        # View
            # app/static
            # app/templates
        # Controller
            # app/controllers

9. Criar o arquivo __init__.py

        # Arquivo para trabalhar com módulos, deverá ser criado para a raiz (/app) e para controllers e models
        # cada init indica módulos

10. CRUD

        # Flask-SQLAlchemy
        - ORM

11. Install Flask-SQLAlchemy

        Instalar dentro do ambiente virtual
        # venv/bin/pip3 install flask-sqlalchemy