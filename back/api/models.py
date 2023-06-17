from django.db import models

# Create your models here.

class Salarie(models.Model):
    id_salarie = models.CharField(primary_key=True, max_length=50)
    first_name = models.CharField(max_length=50,blank=True, null=True)
    last_name = models.CharField(max_length=50,blank=True, null=True)
    phone_number = models.CharField(max_length=50,blank=True, null=True)
    email = models.CharField(max_length=50,blank=True, null=True)
    email_personnal = models.CharField(max_length=50,blank=True, null=True)
    gender = models.CharField(max_length=50,blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'salarie'