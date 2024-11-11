from django.db import models
from User.models import User

class User_Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=255, blank=False)
    caption = models.CharField(max_length=1000)