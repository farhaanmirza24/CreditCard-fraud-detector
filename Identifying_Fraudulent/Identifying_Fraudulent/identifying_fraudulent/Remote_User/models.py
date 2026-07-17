from django.db import models

# Create your models here.
from django.db.models import CASCADE


class ClientRegister_Model(models.Model):

    username = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=10)
    phoneno = models.CharField(max_length=10)
    country = models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)


class detect_fraudulent_cc_transactions(models.Model):

    Fid= models.CharField(max_length=3000)
    Trans_Date= models.CharField(max_length=3000)
    CC_No= models.CharField(max_length=3000)
    CC_type= models.CharField(max_length=3000)
    Trans_Type= models.CharField(max_length=3000)
    Amount= models.CharField(max_length=3000)
    Firstname= models.CharField(max_length=3000)
    Lastname= models.CharField(max_length=3000)
    Gender= models.CharField(max_length=3000)
    Age= models.CharField(max_length=3000)
    lat= models.CharField(max_length=3000)
    lon= models.CharField(max_length=3000)
    Transid= models.CharField(max_length=3000)
    Prediction= models.CharField(max_length=3000)

class detection_ratio(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)

class detection_accuracy(models.Model):

    names = models.CharField(max_length=300)
    ratio = models.CharField(max_length=300)


