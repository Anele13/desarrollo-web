from sqlalchemy import create_engine
from django import forms
import csv, operator
from sqlalchemy import create_engine

def crear():
    engine = create_engine('postgresql://postgres:holamundo@localhost:5432/db_economia', pool_recycle=3600)
    lista_a_borrar=['django_session',
                    'django_migrations',
                    'auth_group',
                    'auth_group_permissions',
                    'auth_permission',
                    'django_content_type',
                    'usuario',
                    'django_permission',
                    'django_admin',
                    'persona_usuario_groups',
                    'persona_usuario_user_permissions',
                    'django_admin_log',
                    'documento']
    diccionario={}
    for tabla in engine.table_names():
        if tabla not in lista_a_borrar:
            diccionario[tabla]=tabla
    return (tuple(diccionario.items()))

class UploadForm(forms.Form):
    tabla= forms.ChoiceField(widget = forms.Select())
    docfile = forms.FileField(label='Selecciona un archivo')

    def __init__(self, *args, **kwargs):
        super(UploadForm, self).__init__(*args, **kwargs)
        self.fields['tabla'] = forms.ChoiceField(choices=crear())
