from django.forms import ModelForm,CharField,PasswordInput,ValidationError
from .models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView


class UsuarioForm(ModelForm):
    class Meta:
        model = Usuario
        exclude = ['usuario']
        
class UserForm(ModelForm):
    password = CharField(widget=PasswordInput(attrs={'placeholder':'Escribe Contraseña'}),label="Contraseña")
    password_re = CharField(widget=PasswordInput(attrs={'placeholder':'Repite Contraseña'}),label="Repite Contraseña")

    class Meta:
        model = User
        fields = ['username','password','password_re']

    def save(self):
        usuario = super(UserForm,self).save()
        usuario.set_password(self.cleaned_data['password'])

    def clean_password(self,*args,**kwargs):
        if self.data['password'] != self.data['password_re']:
            raise ValidationError('Contraseñas No coinciden')
        return self.data['password']

class LoginForm(AuthenticationForm):
    class Meta:
        pass

class HomeForm(ModelForm):
    class Meta:
        pass
