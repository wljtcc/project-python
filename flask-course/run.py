from app import app

# Verifico se o arquivo é o principal, se for secundário, não executa
if __name__ == "__main__":
    app.run(host="0.0.0.0")