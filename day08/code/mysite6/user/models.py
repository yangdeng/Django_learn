from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30,verbose_name='用户名',
                                unique=True)
    password = models.CharField(max_length=30, verbose_name='密码')

    def __str__(self):
        return '用户：'+ self.username