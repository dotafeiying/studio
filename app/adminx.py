# -*- coding:utf-8 -*-
from django.contrib import admin
from .models import Permission,Article,Category, ArticleComment, Type, Notice,EmailVerifyRecord,Picture,About,AboutType
import xadmin
import xadmin.views as xviews
from xadmin.layout import Main, TabHolder, Tab, Fieldset, Row, Col, AppendedText, Side

# Register your models here.
class PermissionAdmin(object):
    list_display = ('name', 'url', 'per_method','describe')

class ArticleCommentAdmin(object):
    list_display = ['user_name','body','article']

class ArticleAdmin(object):
    list_display=['title','last_modified_time','category','type']

class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True
xadmin.site.register(xviews.BaseAdminView, BaseSetting)

class AdminSettings(object):
    # 设置base_site.html的Title
    site_title = '管理后台'
    # 设置base_site.html的Footer
    site_footer = '2017 Admin'
    menu_style = 'default'

    # 菜单设置
    def get_site_menu(self):
        return (
            {'title': '文章管理', 'perm': self.get_model_perm(Article, 'change'), 'menus': (
                {'title': '文章', 'icon': 'fa fa-vimeo-square'
                    , 'url': self.get_model_url(Article, 'changelist')},
                {'title': '考试类别', 'icon': 'fa fa-vimeo-square'
                    , 'url': self.get_model_url(Category, 'changelist')},
                {'title': '文章类别', 'icon': 'fa fa-vimeo-square'
                    , 'url': self.get_model_url(Type, 'changelist')},
                {'title': '文章评论', 'icon': 'fa fa-vimeo-square'
                    , 'url': self.get_model_url(ArticleComment, 'changelist')},
            )},
        )
xadmin.site.register(xviews.CommAdminView, AdminSettings)


class EmailVerifyRecordAdmin(object):
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)

xadmin.site.register(Permission,PermissionAdmin)
xadmin.site.register(ArticleComment,ArticleCommentAdmin)
# xadmin.site.register([Article ,Category, Type, Notice])
xadmin.site.register(Article,ArticleAdmin)
xadmin.site.register(Category)
xadmin.site.register(Type)
xadmin.site.register(Picture)
xadmin.site.register(AboutType)
xadmin.site.register(About)