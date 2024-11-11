from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=20, blank=False, unique=True)
    password = models.CharField(max_length=50, blank=False)
    email = models.CharField(max_length=50, blank=False)

    def __str__(self) -> str:
        return self.username