# api/index.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola Mundo desde Python en Vercel!"

# Esta línea es necesaria para Vercel
if __name__ == '__main__':
    app.run()