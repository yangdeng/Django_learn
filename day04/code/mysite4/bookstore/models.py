from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30, db_index=True,
                             unique=True,
                             verbose_name='书名') #varchar(30)
    pub = models.CharField(max_length=30, verbose_name='出版社',null=True)
    price = models.DecimalField(decimal_places=2,max_digits=7,
                                verbose_name='定价',default=9999) #decimal(7,2)
    maket_price = models.DecimalField(decimal_places=2,max_digits=7,
                                      verbose_name='零售价',default=9999)

    def __str__(self):
        return '书名：'+ self.title

class Author(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField(verbose_name='年龄')
    email = models.EmailField(verbose_name='邮箱')


