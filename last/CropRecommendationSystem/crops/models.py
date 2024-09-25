from django.db import models

class Season(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Crop(models.Model):
    name = models.CharField(max_length=100)
    season = models.ForeignKey(Season, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.name

class Admin(models.Model):
    A_name = models.CharField(max_length=100)
    A_pwd = models.CharField(max_length=100)

    def __str__(self):
        return self.A_name
    
class User(models.Model):
    U_id=models.IntegerField(unique=True)
    U_name = models.CharField(max_length=100)
    U_pwd = models.CharField(max_length=100)
    U_email = models.CharField(max_length=100)

    def __str__(self):
        return self.U_name