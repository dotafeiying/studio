# -*- coding:utf-8 -*-
from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import Article, Category, ArticleComment, Type, Notice,Picture,About,AboutType,EmployeeLife
from .forms import ArticleCommentForm,CkEditorForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required
import markdown,json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class IndexView(ListView):
    template_name = 'app/home.html'
    # 制定获取的model数据列表的名字
    context_object_name = "article_list"

    def get_queryset(self):
        """
        过滤数据，获取已发布文章列表，并转为html格式
        Returns:
        """
        article_list = Article.objects.filter(status='p').order_by('-created_time')[0:6]
        # for article in article_list:
        #     article.comments = len(article.blogcomment_set.all())
        return article_list

    # 为上下文添加额外的变量，以便在模板中访问
    def get_context_data(self, **kwargs):
        kwargs['category_list'] = Category.objects.all().order_by('created_time')
        kwargs['type_list'] = Type.objects.all().order_by('-created_time')
        kwargs['picture_list'] = Picture.objects.all().order_by('pub_date')
        # kwargs['picture_life']= EmployeeLife.objects.all().order_by('CreateTime')[0:4]
        kwargs['picture_life'] = About.objects.filter(category__name='员工生活').order_by('created_time')[0:4]
        kwargs['xyfc_list'] = Picture.objects.all().order_by('pub_date').filter(picture_choices=2)
        kwargs['lbt_list'] = Picture.objects.all().order_by('pub_date').filter(picture_choices=1)
        kwargs['gk_list'] = Article.objects.filter(status='p').filter(category__name='国考',type__name='招考资讯') \
                                .order_by('-created_time')[0:6]
        kwargs['sk_list'] = Article.objects.filter(status='p').filter(category__name='省考',type__name='招考资讯') \
                                .order_by('-created_time')[0:6]
        kwargs['xds_list'] = Article.objects.filter(status='p').filter(category__name='选调生', type__name='招考资讯') \
                                .order_by('-created_time')[0:6]
        kwargs['sy_list'] = Article.objects.filter(status='p').filter(category__name='事业单位', type__name='招考资讯') \
                                .order_by('-created_time')[0:6]
        kwargs['js_list'] = Article.objects.filter(status='p').filter(category__name='教师招考', type__name='招考资讯') \
                                .order_by('-created_time')[0:6]
        kwargs['cg_list'] = Article.objects.filter(status='p').filter(category__name__in=['大学生村官'], type__name='招考资讯') \
                                .order_by('-created_time')[0:6]
        kwargs['gk_beikao_list'] = Article.objects.filter(status='p').filter(category__name='国考').exclude(type__name='招考资讯') \
                                .order_by('-created_time')
        notices=Notice.objects.order_by('-time')
        notice_list=[{'title':notice.title,'body':notice.body} for notice in notices]
        kwargs['notice_list']=json.dumps(notice_list)
        type_list=Type.objects.all().order_by('-created_time')
        bk_list=[]
        for type in type_list:
            bk_list.append(Article.objects.filter(status='p').filter(type__name=type.name) \
                           .order_by('-created_time')[0:7])
        kwargs['bk_list']=bk_list
        return super(IndexView, self).get_context_data(**kwargs)

@login_required
def index1(request):
    return render(request,'app/index1.html')

# def SavePicture(request):
#     if request.method == 'POST':

def ArticleList(request,category,type):
    content={}
    article_list = Article.objects.filter(status='p').filter(type__slug=type,category__slug=category).order_by('-created_time')
    news_list = Article.objects.filter(status='p').filter(category__slug=category, type__name='招考资讯').order_by('-created_time')[0:6]
    top_articles = Article.objects.filter(status='p').filter(category__slug=category).order_by('-likes')[0:9]
    exam_list = Article.objects.filter(status='p').filter(category__slug=category, type__name='真题').order_by('-created_time')[0:6]
    content['news_list'] = news_list
    content['top_articles'] = top_articles
    content['exam_list'] = exam_list
    content['article_list']=article_list
    content['category_list'] = Category.objects.all().order_by('created_time')
    content['type_list'] = Type.objects.all().order_by('-created_time')
    for article in article_list:
        article.comments = len(article.articlecomment_set.all())
    return render(request,'app/list.html',content)

def ArticleOptions(request,category):
    content={}
    article_list = Article.objects.filter(status='p').filter(category__slug=category).order_by('-created_time')
    news_list=Article.objects.filter(status='p').filter(category__slug=category,type__name='招考资讯').order_by('-created_time')[0:6]
    top_articles=Article.objects.filter(status='p').filter(category__slug=category).order_by('-likes')[0:9]
    exam_list=Article.objects.filter(status='p').filter(category__slug=category,type__name='真题').order_by('-created_time')[0:6]
    content['article_list'] = article_list
    content['news_list'] = news_list
    content['top_articles']=top_articles
    content['exam_list']=exam_list
    content['category_list'] = Category.objects.all().order_by('created_time')
    content['type_list'] = Type.objects.all().order_by('-created_time')
    type_list = Type.objects.all().order_by('-created_time')
    article_category_list = []
    for type in type_list:
        article_category_list.append(Article.objects.filter(status='p').filter(type__name=type.name,category__slug=category) \
                       .order_by('-created_time')[0:7])
    content['article_category_list'] = article_category_list
    return render(request,'app/options.html',content)

def ArticleTypes(request,type):
    content = {}
    article_list = Article.objects.filter(status='p').filter(type__slug=type).order_by('-created_time')
    for article in article_list:
        article.comments = len(article.articlecomment_set.all())
    content['article_list'] = article_list
    content['category_list'] = Category.objects.all().order_by('created_time')
    content['type_list'] = Type.objects.all().order_by('-created_time')
    return render(request, 'app/types.html',content)


def detail(request,category,type,pk):
    content={}
    article=Article.objects.filter(status='p').get(pk=pk)
    article.views+=1
    article.save(update_fields=['views'])
    content['article']=article
    content['form']=ArticleCommentForm
    content['comment_list']=article.articlecomment_set.all()
    content['category_list'] = Category.objects.all().order_by('created_time')
    content['type_list'] = Type.objects.all().order_by('-created_time')
    return render(request,'app/detail.html',content)

def CommentView(request,article_id):
    if request.method=='POST':
        form=ArticleCommentForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['user_name']
            # body=markdown.markdown(form.cleaned_data['body'])
            # body = form.cleaned_data['body'].replace('\n', '<br \>')
            body = form.cleaned_data['body']
            article=get_object_or_404(Article,pk=article_id)
            category=article.category.slug
            type=article.type.slug
            ArticleComment(user_name=name,body=body,article=article).save()
            return redirect('app:detail',category=category,type=type,pk=article_id)

def AboutView(request):
    content = {}
    # article_list=About.objects.all()
    news_list = Article.objects.filter(status='p').filter(type__name='招考资讯').order_by(
        '-created_time')[0:6]
    top_articles = Article.objects.filter(status='p').exclude(type__name='招考资讯').order_by('-likes')[0:9]
    exam_list = Article.objects.filter(status='p').filter(type__name='真题').order_by(
        '-created_time')[0:6]
    # content['article_list']=article_list
    content['news_list'] = news_list
    content['top_articles'] = top_articles
    content['exam_list'] = exam_list
    content['category_list'] = Category.objects.all().order_by('created_time')
    content['type_list'] = Type.objects.all().order_by('-created_time')
    type_list = AboutType.objects.all().order_by('-created_time')
    article_type_list = []
    for type in type_list:
        article_type_list.append(About.objects.filter(category__name=type.name).order_by('-created_time'))
    content['article_type_list'] = article_type_list
    return render(request,'app/about/index.html',content)

def AboutList(request,category):
    content={}
    article_list=About.objects.filter(category__slug=category).order_by('-created_time')
    news_list = Article.objects.filter(status='p').filter(type__name='招考资讯').order_by(
        '-created_time')[0:6]
    top_articles = Article.objects.filter(status='p').exclude(type__name='招考资讯').order_by('-likes')[0:9]
    exam_list = Article.objects.filter(status='p').filter(type__name='真题').order_by(
        '-created_time')[0:6]
    content['news_list'] = news_list
    content['top_articles'] = top_articles
    content['exam_list'] = exam_list
    content['article_list']=article_list
    content['category_list'] = Category.objects.all().order_by('created_time')
    content['type_list'] = Type.objects.all().order_by('-created_time')
    return render(request,'app/about/list.html',content)

def AboutDetail(request,category,article_id):
    content={}
    article=About.objects.get(pk=article_id)
    article.views += 1
    article.save(update_fields=['views'])
    content['article']=article
    content['category_list'] = Category.objects.all().order_by('created_time')
    content['type_list'] = Type.objects.all().order_by('-created_time')
    return render(request,'app/about/detail.html',content)

# @csrf_exempt
# def Post_like(request):
#     if request.method=='POST':
#         print(1)
#     article_id=request.GET.get('id')
#     print(article_id)
#     obj=Article.objects.get(pk=int(article_id))
#     obj.likes += 1
#     obj.save()
#     print(obj.likes)
#     return HttpResponse(json.dumps(obj.likes), content_type='application/json')

def Post_like(request):
    # if request.method=='GET':
    # print(article_id)
    print(request)
    article_id=request.GET.get('id')
    obj=Article.objects.get(pk=int(article_id))
    obj.likes += 1
    obj.save()
    return HttpResponse(json.dumps(obj.likes), content_type='application/json')

import django_filters
from rest_framework import viewsets, filters

from .models import Category, Article
from .serializer import CategorySerializer, ArticleSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework import permissions
from rest_framework import generics
from . import APIpermissions

# class Utf8JSONRenderer(JSONRenderer):
#     charset = 'utf-8'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # renderer_classes = (Utf8JSONRenderer,)
    # permission_classes = (permissions.IsAdminUser,)
    permission_classes = (APIpermissions.IsOwnerOrReadOnly,)
