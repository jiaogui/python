from django.db import models
# Create your models here.
class Books(models.Model):
	# 书名
	title = models.CharField(default='', max_length=32)
	# 提供者
	name = models.CharField(default='学校提供', max_length=32)
	# 封面
	img = models.CharField(max_length=64)
	# 价格
	price = models.FloatField()
	# 书的数量
	number_count = models.IntegerField(default='1')
	# 现有书的数量
	number_have = models.IntegerField(default='1')
	# 是否可借
	start= models.SmallIntegerField(default='0')
	# 添加时间
	createTime = models.DateTimeField(auto_now_add=True)
	# 修改时间
	updateTime = models.DateTimeField(auto_now=True)
	def __str__(self):
		return self.title
	class Meta:
		db_table = 'h5_book'
		verbose_name = '图书管理'
		# app_label = 'h5'
		