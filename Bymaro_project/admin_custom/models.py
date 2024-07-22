from django.contrib.auth.models import AbstractUser, Group
from django.db import models


class Chantier(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.nom
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    group = models.ForeignKey(Group, null=True, blank=True, on_delete=models.SET_NULL, related_name='CustomUser')
    chantier = models.ForeignKey(Chantier, null=True, blank=True, on_delete=models.SET_NULL, related_name='CustomUser')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']  # Remove email from REQUIRED_FIELDS

    def __str__(self):
        return self.email



