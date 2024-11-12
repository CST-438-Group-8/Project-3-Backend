from django.db import models

# Create your models here.
from User.models import User
from User_post.models import User_post;

class Comments(models.Model):
  comment_id = models.AutoField(primary_key=True)
  comment = models.CharField(max_length=1000)
  user_id = models.ForeignKey(User, on_delete=models.CASCADE)
  post_id  = models.ForeignKey(User_post, on_delete=models.CASCADE)
