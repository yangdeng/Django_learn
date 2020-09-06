from django.db import models

# Create your models here.
class Publisher(models.Model):
    #出版社是一对多中的一
    name = models.CharField(max_length=50, verbose_name='出版社')

    def __str__(self):
        return  '出版社:'+ self.name


class Book2(models.Model):
    title = models.CharField(max_length=30, verbose_name='书名')
    pub = models.ForeignKey(Publisher, null=True)

    def __str__(self):
        return '书名２:'+ self.title


















