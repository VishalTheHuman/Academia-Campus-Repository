from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()
    file = models.FileField(upload_to='files/')
    permission = models.IntegerField(choices=[(0, 'No Permission'), (1, 'Allow Permission')])

    def __str__(self):
        return f"{self.owner.username}'s File: {self.file.name}"