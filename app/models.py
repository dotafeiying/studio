# -*- coding:utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.utils import timezone
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import  RichTextUploadingField
from datetime import datetime,timedelta

# Create your models here.

class EmailVerifyRecord(models.Model):
    email_choices = (
        ('register', u'注册'),
        ('forget', u'找回密码'),
    )
    code = models.CharField(max_length=20, verbose_name=u'验证码')
    email = models.EmailField(max_length=50, verbose_name=u'邮箱')
    send_type = models.CharField(choices=email_choices, max_length=10, verbose_name=u'验证码类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name=u'发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

class Permission(models.Model):
    name = models.CharField("权限名称", max_length=64)
    url = models.CharField('URL名称', max_length=255)
    chioces = ((1, 'GET'), (2, 'POST'))
    per_method = models.SmallIntegerField('请求方法', choices=chioces, default=1)
    argument_list = models.CharField('参数列表', max_length=255, help_text='多个参数之间用英文半角逗号隔开', blank=True, null=True)
    describe = models.CharField('描述', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '权限表'
        verbose_name_plural = verbose_name
        #权限信息，这里定义的权限的名字，后面是描述信息，描述信息是在django admin中显示权限用的
        permissions = (
            ('views_student_list', '查看学员信息表'),
            ('views_student_info', '查看学员详细信息'),
        )

class Category(models.Model):
    """
    另外一个表,储存文章的分类信息
    文章表的外键指向
    """
    name = models.CharField('考试类别', max_length=20)
    slug = models.CharField('考试栏目网址', max_length=255, db_index=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def get_absolute_url(self):
        return reverse('category', args=(self.slug,))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章大类'
        verbose_name_plural = verbose_name

class Type(models.Model):
    """
    另外一个表,储存文章的分类信息
    文章表的外键指向
    """
    name = models.CharField('文章类别', max_length=20)
    slug = models.CharField('文章栏目网址', max_length=255, db_index=True)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    last_modified_time = models.DateTimeField('修改时间', auto_now=True)

    def get_absolute_url(self):
        return reverse('type', args=(self.slug,))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章小类'
        verbose_name_plural = verbose_name

class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'part'),
        ('p', 'Published'),
    )  # 文章的状态

    title = models.CharField('标题', max_length=100)
    # body = models.TextField('正文')

    # body = RichTextField("正文")

    body = RichTextUploadingField("正文")
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    # auto_now_add : 创建时间戳，不会被覆盖

    last_modified_time = models.DateTimeField('修改时间', auto_now=True)
    # auto_now: 自动将当前时间覆盖之前时间

    status = models.CharField('文章状态', max_length=1, choices=STATUS_CHOICES)
    abstract = models.CharField('摘要', max_length=54, blank=True, null=True,
                                help_text="可选项，若为空格则摘取正文钱54个字符")
    site = models.CharField('官网', max_length=100, default='楚公教育网')
    author = models.CharField('作者', max_length=100, default='扬帆起航')
    source = models.CharField('来源', max_length=100, default='扬帆起航工作室')
    # 阅读量
    views = models.PositiveIntegerField('浏览量', default=0)
    # 点赞数
    likes = models.PositiveIntegerField('点赞数', default=0)
    # 是否置顶
    topped = models.BooleanField('置顶', default=False)
    # 目录分类
    # on_delete 当指向的表被删除时，将该项设为空
    category = models.ForeignKey('Category', verbose_name='考试类别',
                                 null=True,
                                 on_delete=models.SET_NULL)
    type = models.ForeignKey('Type', verbose_name='文章类别',
                                 null=True,
                                 on_delete=models.SET_NULL)

    def __str__(self):
        return self.title

    class Meta:
        # Meta 包含一系列选项，这里的ordering表示排序, - 表示逆序
        # 即当从数据库中取出文章时，以文章最后修改时间逆向排序
        ordering = ['-last_modified_time']
        verbose_name = '文章'
        verbose_name_plural = verbose_name

    def get_absolute_url(self):
        return reverse('app:detail', kwargs={'article_id': self.pk})

    def save(self, *args, **kwargs):
        self.abstract=self.body[:54]
        super(Article, self).save(*args, **kwargs)

class ArticleComment(models.Model):
    user_name = models.CharField('评论者名字', max_length=100)
    body = models.TextField('评论内容')
    created_time = models.DateTimeField('评论发表时间', auto_now_add=True)
    article = models.ForeignKey('Article', verbose_name='评论所属文章', on_delete=models.CASCADE)

    def __str__(self):
        return self.body[:20]

    class Meta:
        verbose_name = '文章评论'
        verbose_name_plural = verbose_name

class Notice(models.Model):
    title = models.CharField('标题', max_length=100)
    body = models.TextField('正文')
    time = models.DateTimeField('时间', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '网站公告'
        verbose_name_plural = verbose_name

class Picture(models.Model):
    title = models.CharField(max_length = 50)
    picture = models.ImageField(upload_to = 'pictures')
    picture_choices = models.CharField('图片类型', max_length=1, choices=(('1', '轮播图'), ('2', '广告')))
    pub_date = models.DateTimeField('date published',default=timezone.now)
    describe = models.CharField('描述', max_length=255,null=True,blank=True)


    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=1) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

    def __str__(self):
        return self.title

    class Meta:
        db_table = "picture"
        verbose_name = '图片'
        verbose_name_plural = verbose_name

class About(models.Model):
    title = models.CharField(max_length = 50)
    slug = models.CharField('类别网址', max_length=255, db_index=True,default='about')
    body = RichTextUploadingField("正文")
    Attachment = models.ImageField(verbose_name='图片上传', upload_to='pictures', null=True, blank=True)
    created_time = models.DateTimeField('创建时间',default=timezone.now)
    site = models.CharField('官网', max_length=100, default='楚公教育网')
    author = models.CharField('作者', max_length=100, default='扬帆起航')
    source = models.CharField('来源', max_length=100, default='扬帆起航工作室')
    # 阅读量
    views = models.PositiveIntegerField('浏览量', default=0)
    category = models.ForeignKey('AboutType', verbose_name='关于类别',
                                 null=True,
                                 on_delete=models.SET_NULL)
    class Meta:
        verbose_name = '关于'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

class AboutType(models.Model):
    name = models.CharField('关于类别名', max_length=20)
    slug = models.CharField('网址', max_length=255, db_index=True)
    created_time = models.DateTimeField('创建时间', default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '关于类型'
        verbose_name_plural = verbose_name

class EmployeeLife(models.Model):
    Title = models.CharField(verbose_name='图片说明', max_length=100)
    body = RichTextUploadingField("正文", null=True, blank=True)
    Attachment = models.ImageField(verbose_name='图片上传',upload_to = 'pictures')
    CreateTime = models.DateTimeField(verbose_name='新增时间', auto_now_add=True)
    ModifyTime = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    def __str__(self):
        return self.Title

    class Meta:
        verbose_name_plural = verbose_name = '员工生活'
