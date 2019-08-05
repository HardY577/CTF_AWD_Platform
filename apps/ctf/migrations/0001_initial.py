# Generated by Django 2.1.7 on 2019-08-05 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CtfLibrary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ctf_type', models.IntegerField(choices=[(0, 'WEB'), (1, 'REVERSE'), (2, 'MISC'), (3, 'STEGA'), (4, 'PWN'), (5, 'CRYPTO'), (6, 'PPC')], default=0, verbose_name='题目类型')),
                ('ctf_title', models.CharField(max_length=30, null=True, verbose_name='题目标题')),
                ('ctf_description', models.TextField(max_length=255, null=True, verbose_name='题目描述')),
                ('ctf_score', models.IntegerField(default=0, verbose_name='题目分数')),
                ('ctf_address', models.CharField(max_length=255, null=True, verbose_name='题目地址')),
                ('ctf_flag', models.CharField(max_length=255, null=True, verbose_name='flag')),
            ],
            options={
                'verbose_name': '题库',
                'verbose_name_plural': '题库',
            },
        ),
    ]
