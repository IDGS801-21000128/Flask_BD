from flask import Flask, render_template, request, flash
import forms
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    alumno_clase = forms.UserForm(request.form)
    nom = ""
    apa = ""
    ama = ""
    edad = None
    if request.method=='POST' and alumno_clase.validate():
        nom=alumno_clase.nombre.data
        
        apa=alumno_clase.apaterno.data
        ama=alumno_clase.amaterno.data
        edad=alumno_clase.edad.data
        print('Nombre: {}'.format(nom))
        print('apaterno: {}'.format(apa))
        print('amaterno: {}'.format(ama))

        mensaje = 'Bienvenido {}'.format(nom)
        flash(mensaje)
    return render_template("alumnos.html", form=alumno_clase, nom=nom, apa=apa, ama=ama, edad=edad)

if __name__ == "__main__":
    csrf.init_app(app)

    app.run()
