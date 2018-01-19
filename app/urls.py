"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.decorators import login_required

app_name = 'app'
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', login_required(views.IndexView.as_view()), name='index'),
    # url(r'^accounts/login/$', login),
    # url(r'^logout/$', logout, {'next_page': '/login/'}),
    url(r'^index/$', views.index1, name='index1'),
    url(r'^detail/(?P<category>\w+)/$', views.ArticleOptions, name='options'),
    url(r'^type/(?P<type>\w+)/$', views.ArticleTypes, name='type'),
    url(r'^detail/(?P<category>\w+)/(?P<type>\w+)/$', views.ArticleList, name='list'),
    url(r'^detail/(?P<category>\w+)/(?P<type>\w+)/(?P<pk>\d+)/$', views.detail, name='detail'),
    url(r'^article/(?P<article_id>\d+)/comment/$', views.CommentView, name='comment'),
    url(r'^article/like/add/$', views.Post_like, name='like'),
    url(r'^about/$', views.AboutView, name='about'),
    url(r'^about/(?P<category>\w+)/$', views.AboutList, name='aboutlist'),
    url(r'^about/(?P<category>\w+)/(?P<article_id>\d+)/$', views.AboutDetail, name='aboutdetail'),

    # url(r'^article/(?P<article_id>[0-9]+)/$',views.ArticleDetailView.as_view(),name='detail'),
    # url(r'^article/(?P<article_id>\d+)/comment/$', views.CommentView, name='comment'),
    # url(r'^article/like/$', views.Post_like, name='like'),
    # url(r'^like/$', views.Post_like, name='like'),


    # url(r'^$', views.index, name='index'),
    # url(r'^profile/', views.SaveProfile, name='saveprofile'),
    # url(r'^saved/', TemplateView.as_view(template_name='myapp/saved.html'), name='saved'),
    # url(r'^upload_page/$', views.upload_page,name='upload_page'),
    # url(r'^upload/$', views.upload,name='upload'),
    # url(r'^table/$', views.table,name='table'),
    # url(r'^add/$', views.add,name='add'),
    # url(r'^export/$', views.excel_export,name='export')
]

from rest_framework import routers
from .views import CategoryViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register(r'category', CategoryViewSet)
router.register(r'article', ArticleViewSet)
