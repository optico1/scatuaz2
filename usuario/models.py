from django.db import models
from django.contrib.auth.models import AbstractUser

class UserSCATUAZ(AbstractUser):

    materno = models.CharField(
        max_length=50,
    )
    
