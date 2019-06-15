from django.db import models
# Create your models here.
class Nav(models.Model):
	name = models.CharField(default='', max_length=32)
	img = models.CharField(default='', max_length=64)
	href = models.CharField(default='', max_length=32)
	pid = models.SmallIntegerField(default='0')
	createTime = models.DateTimeField(auto_now_add=True)
	updateTime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.name
	class Meta:
		db_table = 'h5_nav'
		verbose_name = '菜单兰目'
		# app_label = 'h5'