# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-30 01:24
from __future__ import unicode_literals

import ckeditor_uploader.fields
import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.CharField(db_index=True, default='about', max_length=255, verbose_name='类别网址')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文')),
                ('Attachment', models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='图片上传')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
            options={
                'verbose_name': '关于',
                'verbose_name_plural': '关于',
            },
        ),
        migrations.CreateModel(
            name='AboutType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章类别')),
                ('slug', models.CharField(db_index=True, max_length=255, verbose_name='文章栏目网址')),
                ('created_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='创建时间')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
                ('status', models.CharField(choices=[('d', 'part'), ('p', 'Published')], max_length=1, verbose_name='文章状态')),
                ('abstract', models.CharField(blank=True, help_text='可选项，若为空格则摘取正文钱54个字符', max_length=54, null=True, verbose_name='摘要')),
                ('site', models.CharField(default='楚公教育网', max_length=100, verbose_name='官网')),
                ('author', models.CharField(default='扬帆起航', max_length=100, verbose_name='作者')),
                ('source', models.CharField(default='扬帆起航工作室', max_length=100, verbose_name='来源')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
                ('likes', models.PositiveIntegerField(default=0, verbose_name='点赞数')),
                ('topped', models.BooleanField(default=False, verbose_name='置顶')),
            ],
            options={
                'verbose_name_plural': '文章',
                'verbose_name': '文章',
                'ordering': ['-last_modified_time'],
            },
        ),
        migrations.CreateModel(
            name='ArticleComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100, verbose_name='评论者名字')),
                ('body', models.TextField(verbose_name='评论内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='评论发表时间')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Article', verbose_name='评论所属文章')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='考试类别')),
                ('slug', models.CharField(db_index=True, max_length=255, verbose_name='考试栏目网址')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.CreateModel(
            name='EmailVerifyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_type', models.CharField(choices=[('register', '注册'), ('forget', '找回密码')], max_length=10, verbose_name='验证码类型')),
                ('send_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='发送时间')),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
        migrations.CreateModel(
            name='EmployeeLife',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100, verbose_name='图片说明')),
                ('body', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='正文')),
                ('Attachment', models.ImageField(blank=True, null=True, upload_to='pictures', verbose_name='图片上传')),
                ('CreateTime', models.DateTimeField(auto_now_add=True, verbose_name='新增时间')),
                ('ModifyTime', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '员工生活',
                'verbose_name_plural': '员工生活',
            },
        ),
        migrations.CreateModel(
            name='Notice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('body', models.TextField(verbose_name='正文')),
                ('time', models.DateTimeField(auto_now=True, verbose_name='时间')),
            ],
        ),
        migrations.CreateModel(
            name='Permission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='权限名称')),
                ('url', models.CharField(max_length=255, verbose_name='URL名称')),
                ('per_method', models.SmallIntegerField(choices=[(1, 'GET'), (2, 'POST')], default=1, verbose_name='请求方法')),
                ('argument_list', models.CharField(blank=True, help_text='多个参数之间用英文半角逗号隔开', max_length=255, null=True, verbose_name='参数列表')),
                ('describe', models.CharField(max_length=255, verbose_name='描述')),
            ],
            options={
                'permissions': (('views_student_list', '查看学员信息表'), ('views_student_info', '查看学员详细信息')),
                'verbose_name': '权限表',
                'verbose_name_plural': '权限表',
            },
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='pictures')),
                ('picture_choices', models.CharField(choices=[('1', '轮播图'), ('2', '学员风采')], max_length=1, verbose_name='图片类型')),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('describe', models.CharField(max_length=255, verbose_name='描述')),
            ],
            options={
                'verbose_name': '图片',
                'db_table': 'picture',
                'verbose_name_plural': '图片',
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章类别')),
                ('slug', models.CharField(db_index=True, max_length=255, verbose_name='文章栏目网址')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Category', verbose_name='考试类别'),
        ),
        migrations.AddField(
            model_name='article',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.Type', verbose_name='文章类别'),
        ),
        migrations.AddField(
            model_name='about',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.AboutType', verbose_name='考试类别'),
        ),
    ]
