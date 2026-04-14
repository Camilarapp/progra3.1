
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    lista=['La guitarra', 'Para no verte mas', 'Balada para un gordo']
    return render_template('lista.html', titulo= 'canciones', musicas=listas)

