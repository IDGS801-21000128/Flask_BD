from flask import Flask, render_template, request, flash
import forms
from flask_wtf.csrf import CSRFProtect
from flask import g
from config import DevelopmentConfig
from models import db
from models import Alumnos

app=Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"),404

#@app.route("/")
#def index():
#    return render_template("index.html")

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

@app.route('/index', methods=['GET', 'POST'])
def index():
    create_forms=forms.UserForm2(request.form)
    if request.method=='POST':
        alumn=Alumnos(nombre=create_forms.nombre.data,
            apaterno=create_forms.apaterno.data,
            email=create_forms.email.data)
        db.session.add(alumn)
        db.session.commit()
    return render_template('index.html', form=create_forms)

@app.route("/ABC_Completo", methods=["GET","POST"])
def ABCompleto():
    alum_form = forms.UserForm2(request.form)
    alumno = Alumnos.query.all()
    return render_template("ABC_Completo.html", alumno=alumno, alum_form=alum_form)

@app.route('/eliminar', methods=['GET', 'POST'])
def eliminar():
    create_form = forms.UserForm2(request.form)
    if request.method=='GET':
        id=request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        create_form.id.data = request.args.get('id')
        create_form.nombre.data = alum1.nombre
        create_form.apaterno.data = alum1.apaterno
        create_form.email.data = alum1.email
    if request.method == 'POST':
        id = create_form.id.data
        alum = Alumnos.query.get(id)


if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()
    app.run()
