from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Datos de ejemplo
posts = [
    {
        'titulo': 'Mi primer post',
        'autor': 'Daniel',
        'fecha': '2024-03-15',
        
    },
    {
        'titulo': 'Programación Distribuida',
        'autor': 'Daniel Clavijo',
        'fecha': '2024-03-16',
        
    }
]

@app.route('/')
def inicio():
    return render_template('inicio.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', titulo='Sobre Nosotros')

@app.route('/contacto')
def contacto():
    return render_template('contacto.html', titulo='Contacto')

if __name__ == '__main__':
    app.run(debug=True)