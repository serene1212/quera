from django.db import models
class Author(models.Model):
    name=models.CharField(max_length=25)
class Book(models.Model):
    date=models.DateFiled()
    name=models.CharField(max_length=25)
    author=models.ManyToManyField(Author)
class Profile(models.Model):
    email=models.EmailField()
    passw=models.CharField(max_length=25)
class Lib(models.Model):
    number=models.IntegerField()
class Personel(models.Model):
    profile=models.OneToOneField(Profile,on_delete=models.CASCADE)
    lib=models.ForeignKey(Lib,on_delete=models.CASCADE)
