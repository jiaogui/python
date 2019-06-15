# Generated by Django 2.2 on 2019-06-15 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32)),
                ('img', models.CharField(default='', max_length=64)),
                ('href', models.CharField(default='', max_length=32)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '菜单兰目',
                'db_table': 'h5_nav',
            },
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=32)),
                ('pwd', models.CharField(default='', max_length=64)),
                ('token', models.CharField(default='', max_length=64)),
                ('createTime', models.DateTimeField(auto_now_add=True)),
                ('updateTime', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': '前端用户表',
                'db_table': 'h5_user',
            },
        ),
    ]