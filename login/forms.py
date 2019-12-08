from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django import forms


class UserForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Escribe contraseña'
            }
        ),
        label="Contraseña"
    )
    password_re = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repite contraseña'
            }
        ),
        label="Repita contraseña"
    )

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password', 'password_re']

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

    def clean_password(self, *args, **kwargs):
        if self.data['password'] != self.data['password_re']:
            raise forms.ValidationError(
                'Las contraseñas no son iguales',
                code='passwords_not_equals')
        return self.data['password']


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=50,
        min_length=5,
        widget=forms.TextInput({
            'class': 'form-control',
            'placeholder': 'Nombre de usuario',
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'max_length': 'La longitud maxima es de 50',
            'min_length': 'La longitud minima es de 5'
        }
    )
    password = forms.CharField(
        max_length=16,
        min_length=8,
        widget=forms.PasswordInput({
            'class': 'form-control',
            'placeholder': 'Contraseña',
        }),
        error_messages={
            'required': 'Este campo es obligatorio',
            'max_length': 'La longitud maxima es de 16',
            'min_length': 'La longitud minima es de 8'
        }
    )

    def __init__(self, *args, **kwargs):
        self.error_messages['invalid_login'] = 'Credenciales invalidas'
        super().__init__(*args, **kwargs)

    class Meta:
        fields = '__all__'
