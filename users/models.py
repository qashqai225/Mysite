from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    img = models.ImageField(default='user_images/default.gif', upload_to='user_images')
    tell = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return f"Сторінка користувача: {self.user.username}"
