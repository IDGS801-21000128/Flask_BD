from wtforms import Form
from wtforms import StringField, EmailField, IntegerField
from wtforms import validators

class UserForm(Form):
    nombre = StringField('nombre', [
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=19, message='ingresa nombre valido')
    ])

    apaterno = StringField('apaterno',{
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=19, message='ingresa apellido paterno valido')
    })
    amaterno = StringField('amaterno', {
        validators.DataRequired(message='El campo es requerido'),
        validators.length(min=4, max=19, message='ingresa apellido materno valido')
    })
    email = EmailField('email', [validators.Email(message='Ingrese un correo valido')])
    edad= IntegerField('edad', {
        validators.DataRequired(message='El campo es requerido')
    })