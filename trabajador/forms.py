from .models import Trabajador, OPCIONES_SEXO, OPCIONES_ESTADO_CIVIL, OPCIONES_STATUS
from django.forms import ModelForm, Textarea, TextInput, NumberInput, Select, DateInput, DateField, EmailInput, SelectDateWidget


class TrabajadorForm(ModelForm):
    class Meta:
        model = Trabajador
        fields = '__all__'

        widgets = {
            'paterno': TextInput(attrs={'class':'form-control'}),
            'materno': TextInput(attrs={'class':'form-control'}),
            'nombre': TextInput(attrs={'class':'form-control'}),
            'rfc': TextInput(attrs={'class':'form-control'}),
            'curp': TextInput(attrs={'class':'form-control'}),
            'sexo': Select(choices=OPCIONES_SEXO, attrs={'class':'form-control'}),
            'estado_civil': Select(choices=OPCIONES_ESTADO_CIVIL, attrs={'class':'form-control'}),
            'status': Select(choices=OPCIONES_STATUS, attrs={'class':'form-control'}),
            'curp': TextInput(attrs={'class':'form-control'}),
            'fecha_nacimiento': DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control'}),
            'pais_nacimiento': TextInput(attrs={'class':'form-control'}),
            'estado_nacimiento': NumberInput(attrs={'class':'form-control'}),
            'municipio_nacimiento': NumberInput(attrs={'class':'form-control'}),
            'lugar_nacimiento': TextInput(attrs={'class':'form-control'}),
            'pais_residencia': TextInput(attrs={'class':'form-control'}),
            'estado_residencia': NumberInput(attrs={'class':'form-control'}),
            'municipio_residencia': NumberInput(attrs={'class':'form-control'}),
            'localidad_reside': TextInput(attrs={'class':'form-control'}),
            'calle': TextInput(attrs={'class':'form-control'}),
            'colonia': TextInput(attrs={'class':'form-control'}),
            'cp': TextInput(attrs={'class':'form-control'}),
            'telefono': TextInput(attrs={'class':'form-control'}),
            'email': EmailInput(attrs={'class':'form-control'}),
        }