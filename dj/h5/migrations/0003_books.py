# Generated by Django 2.2 on 2019-06-17 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('h5', '0002_auto_20190617_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=32)),
                ('name', models.CharField(default='学校提供', max_length=32)),
                ('img', models.CharField(max_length=64)),
                ('price', models.FloatField()),
                ('number_count', models.IntegerField(default='1')),
                ('number_have', models.IntegerField(default='1')),
                ('start', models.SmallIntegerField(default='0')),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '图书管理',
                'db_table': 'h5_book',
            },
        ),
    ]