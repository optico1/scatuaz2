from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django.contrib.auth.models import User

class UsuarioForm(UserCreationForm):

    username = forms.CharField(
        max_length=50,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Escribe el usuario',
                'class': 'form-control form-control-sm'
            }
        ),
        error_messages={
            'required': 'El campo Usuario es obligatorio',
            'max_length': 'La longitud maxima es de 50',
            'min_length': 'La longitud minima es de 5',
        },
        label="Usuario"
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Escribe el correo',
                'class': 'form-control form-control-sm'
            }
        ),
        error_messages={
            'required': 'El campo Correo es obligatorio',
        },
        label="Correo"
    )

    password1 = forms.CharField(
        max_length=16,
        min_length=8,
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Escribe la contraseña',
                'class': 'form-control form-control-sm'
            }
        ),
        error_messages={
            'required': 'El campo Contraseña es obligatorio',
            'max_length': 'La longitud maxima es de 16',
            'min_length': 'La longitud minima es de 8',
        },
        label="Contraseña"
    )

    password2 = forms.CharField(
        required=True,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Repite la contraseña',
                'class': 'form-control form-control-sm'
            }
        ),
        error_messages={
            'required': 'El campo Contraseña es obligatorio',
        },
        label="Repita contraseña"
    )

    is_superuser = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input'
            }
        ),
        label="¿El usuario sera administrador?"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'is_superuser']

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

    def clean_password(self, *args, **kwargs):
        if self.data['password1'] != self.data['password2']:
            raise forms.ValidationError(
                'Las contraseñas no son iguales',
                code='passwords_not_equals')
        return self.data['password1']

class CambiarContrasenaForm(SetPasswordForm):

    new_password1 = forms.CharField(
        max_length=16,
        min_length=8,
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-sm'
            }
        ),
        error_messages={
            'max_length': 'La longitud maxima es de 16',
            'min_length': 'La longitud minima es de 8',
        },
        label="Nueva Contraseña"
    )

    new_password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control form-control-sm'
            }
        ),
        label="Repita Nueva contraseña"
    )


class ModificarUsuarioForm(UserChangeForm):

    username = forms.CharField(
        max_length=50,
        min_length=5,
        required=True,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Escribe el usuario',
                'class': 'form-control form-control-sm'
            }
        ),
        error_messages={
            'required': 'El campo Usuario es obligatorio',
            'max_length': 'La longitud maxima es de 50',
            'min_length': 'La longitud minima es de 5',
        },
        label="Usuario"
    )

    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'placeholder': 'Escribe el correo',
                'class': 'form-control form-control-sm'
            }
        ),
        error_messages={
            'required': 'El campo Correo es obligatorio',
        },
        label="Correo"
    )

    is_superuser = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input'
            }
        ),
        label="¿El usuario sera administrador?"
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'is_superuser']

    def save(self, commit=True):
        user = super(ModificarUsuarioForm, self).save(commit=False)
        if commit:
            user.save()
        return user