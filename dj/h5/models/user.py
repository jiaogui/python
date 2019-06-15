from django.db import models
# Create your models here.
class user(models.Model):
	name = models.CharField(default='', max_length=32)
	pwd = models.CharField(default='', max_length=64)
	token = models.CharField(default='', max_length=64)
	createTime = models.DateTimeField(auto_now_add=True)
	updateTime = models.DateTimeField(auto_now=True)
	class Meta:
		db_table = 'h5_user'
		verbose_name = '前端用户表'
		# app_label = 'h5'