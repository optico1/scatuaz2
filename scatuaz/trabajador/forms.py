from .models import Trabajador, OPCIONES_SEXO, OPCIONES_ESTUDIOS 
from django import forms


class TrabajadorForm(forms.ModelForm):
    # DATOS PERSONALES
    paterno = forms.CharField(
        required=True,
        label='Apellido Paterno',
        error_messages={
            'required': 'El campo Apellido Paterno es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    materno = forms.CharField(
        required=True,
        label='Apellido Materno',
        error_messages={
            'required': 'El campo Apellido Materno es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    nombre = forms.CharField(
        required=True,
        label='Nombre',
        error_messages={
            'required': 'El campo Nombre es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    rfc = forms.CharField(
        required=True,
        label='RFC',
        max_length=13,
        error_messages={
            'required': 'El campo RFC es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    curp = forms.CharField(
        required=True,
        label='CURP',
        error_messages={
            'required': 'El campo CURP es obligatorio',
        },
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    sexo = forms.ChoiceField(
        required=True,
        label='Sexo',
        choices=OPCIONES_SEXO, 
        widget=forms.RadioSelect(
            attrs={'class': 'form-check-input'},
        )
    )
    pais_residencia = forms.CharField(
        required=True,
        label='País de Residencia',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    estado_residencia = forms.CharField(
        required=True,
        label='Estado de Residencia',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    municipio_residencia = forms.CharField(
        required=True,
        label='Municipio de Residencia',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    calle = forms.CharField(
        required=True,
        label='Calle de Residencia',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    numero = forms.CharField(
        required=True,
        label='Numero',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    colonia = forms.CharField(
        required=True,
        label='Colonia de Residencia',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    cp = forms.CharField(
        required=True,
        label='CP',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    telefono = forms.CharField(
        required=False,
        max_length=10,
        label='Teléfono',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    email = forms.CharField(
        required=False,
        label='Correo Electronico',
        widget=forms.EmailInput(
            attrs={'class': 'form-control'}
        )
    )
    # DATOS LABORALES
    matricula_administrativo = forms.CharField(
        required=True,
        max_length=6,
        label='Matricula de Administrativo',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    matricula_gremial = forms.CharField(
        required=True,
        max_length=6,
        label='Matricula Gremial',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    # DATOS ACADEMICOS
    grado_max_estudios = forms.ChoiceField(
        required=True,
        label='Grado Max de Estudios',
        choices=OPCIONES_ESTUDIOS, 
        widget=forms.Select(
            attrs={'class': 'form-control'},
        )
    )
    # DATOS ISSSTE
    nss = forms.CharField(
        required=True,
        max_length=11,
        label='NSS',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    no_issste = forms.CharField(
        required=True,
        label='No. de ISSSTE',
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    # REGISTROS
    validado_renapo = forms.BooleanField(
        required=False,
        label='Validado por RENAPO',
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input'}
        )
    )
    validado_siri = forms.BooleanField(
        required=False,
        label='Validado por SIRI',
        widget=forms.CheckboxInput(
            attrs={'class': 'form-check-input',}
        )
    )
    alta_usuario = forms.CharField(
        required=False
    )
    

    class Meta:
        model = Trabajador
        exclude = ('alta_usuario',)
