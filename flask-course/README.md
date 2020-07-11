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
        # venv/bin/pip3 install psycopg2-binary

11. Migrations

        Flask-Migrate
        Flask-Script
        # venv/bin/pip3 install flask-migrate
        # venv/bin/pip3 install flask-script

  11.1. Usando o MIGRATE, deverá ser modificado como a aplicação é executada:

        # Para executar a aplicação: python3 run.py runserver
        # Iniciar o Banco: python3 run.py db init
        # Executar os migratios de comparação: python3 run.py db migrate
        # Executar os migratios de inserção ou update: python3 run.py db upgrade

12. Forms

        # Para forms no Flask, deveremos instalar o FlaskWTF
        # venv/bin/pip3 install flask-wtf