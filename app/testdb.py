# -*- coding: utf-8 -*-
import os,django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','studio.settings')
django.setup()

from app.models import Article,Category,About,AboutType

# blog=BlogComment.objects.get(id=37)
# print(blog)
# article_list=Article.objects.all()
# print(article_list)
# for article in article_list:
#     article.comments=len(article.blogcomment_set.all())
# print(article_list)
# print([(x.title,x.comments) for x in article_list])

# article=Article.objects.filter(status='p').filter(category__slug='szyf',type__slug='jz').get(pk=1053)
# print(article.category.slug)
# type_list = AboutType.objects.all().order_by('-created_time')
# article_type_list = []
# for type in type_list:
#     article_type_list.append(About.objects.filter(category=type.name).order_by('-created_time')[0:7])
a=About.objects.filter(category__name='关于我们').order_by('-created_time')[0:7]

print(a)
