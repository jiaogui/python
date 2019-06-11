from django.db import models
# Create your models here.
class user(models.Model):
	name = models.CharField( max_length=20)
	token = models.CharField( max_length=20)
	createTime = models.CharField( max_length=20)