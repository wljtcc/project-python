import os
from app import manager

# Verifico se o arquivo é o principal, se for secundário, não executa
if __name__ == "__main__":
    # app.run(
    #     host = os.getenv('FLASK_RUN_HOST'),
    #     port = os.getenv('FLASK_RUN_PORT')
    #     )
    manager.run()
    