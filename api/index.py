# api/index.py
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Datos de ejemplo
posts = [
    {
        'titulo': 'Mi primer post',
        'autor': 'Juan',
        'fecha': '2024-03-15',
        'contenido': 'Este es el contenido de mi primer post en el blog.'
    },
    {
        'titulo': 'Aprendiendo Flask',
        'autor': 'María',
        'fecha': '2024-03-16',
        'contenido': 'Flask es un framework muy interesante para crear aplicaciones web.'
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

# Esta línea es importante para Vercel
app.static_folder = 'static'

if __name__ == '__main__':
    app.run(debug=True)