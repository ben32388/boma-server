from django.db import models
from users.models import User


class Folder(models.Model):
    title = models.CharField('名稱', max_length=50) 
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='使用者')
    
    def __str__(self):
        return self.title
