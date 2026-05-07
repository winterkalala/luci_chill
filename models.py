from django.db import models
from django.contrib.auth.hashers import make_password
#from django.utils import timezone

# Create your models here.

#Creation de la table Compte Etablissement 
class Etablissement(models.Model):
    username = models.CharField(max_length=100, unique=True)
    pwd = models.CharField(max_length=128)
    adresse = models.TextField()
    description = models.TextField()
    Email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/')
    cate = models.CharField(max_length=50)
    date_create=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Si l'utilisateur est nouveau
            self.pwd = make_password(self.pwd)  # Hachage du mot de passe
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username

    
class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    pwd = models.CharField(max_length=128)
    Email = models.EmailField(unique=True)
    city = models.CharField(max_length=100)
    image = models.ImageField()
    date_create=models.DateTimeField(auto_now_add=True)
    date_update=models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # Si l'utilisateur est nouveau
            self.pwd = make_password(self.pwd)  # Hachage du mot de passe
        super().save(*args, **kwargs)

    def __str__(self):
        return self.username



#-_-_-_-_-_-_-__-_-_-_-_-_-_-__-_-_-_-_-_-__-_-_-_-_-__--_-_-_-_-_-_-_-_-_-_-_-_-_



"""

class service(models.Model):

class publication(models.Model):

class comment(models.Model):

class menu_b(models.Model):

class menu_B(models.Model): "
    ""

"""