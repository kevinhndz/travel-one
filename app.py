import os
import mimetypes
mimetypes.add_type('text/css','.css')
from flask import Flask, render_template, request, redirect, url_for, session
from flask_pymongo import PyMongo
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

app.jinja_env.globals.update(enumerate=enumerate)

ADMIN_USER = "admin"
ADMIN_PASS = "travel2026"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contacto', methods=['GET', 'POST'])
def contacto():
    if request.method == 'POST':
        interesado = {
            "nombre_cliente": request.form['nombre'],
            "telefono":       request.form['telefono'],
            "destino":        request.form['destino'],
            "fecha_v":        request.form['fecha'],
            "Comment":        request.form['detalles']
        }
        mongo.db.clientes.insert_one(interesado)
        return render_template('contact_us.html', nombre=interesado["nombre_cliente"])
    return render_template('contact_us.html', nombre=None)

@app.route('/admin', methods=['GET', 'POST'])
def admin_login():
    error = None
    if request.method == 'POST':
        if request.form['user'] == ADMIN_USER and request.form['password'] == ADMIN_PASS:
            session['admin'] = True
            return redirect(url_for('admin_panel'))
        error = "Credenciales incorrectas"
    return render_template('admin_login.html', error=error)

@app.route('/admin/panel')
def admin_panel():
    if not session.get('admin'):
        return redirect(url_for('admin_login'))
    clientes = list(mongo.db.clientes.find())
    return render_template('admin_panel.html', clientes=clientes)

@app.route('/admin/logout')
def admin_logout():
    session.pop('admin', None)
    return redirect(url_for('admin_login'))

if __name__ == '__main__':
    app.run(debug=True)