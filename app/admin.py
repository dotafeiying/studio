from django.contrib import admin
from .models import Permission,Article,Category, ArticleComment, Type, Notice, Picture,About,AboutType,EmployeeLife

# Register your models here.
class PermissionAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'per_method','describe')

class ArticleCommentAdmin(admin.ModelAdmin):
    list_display = ['user_name','body','article']

class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title','category','type','views','likes']

class PictureAdmin(admin.ModelAdmin):
    list_display = ['title','picture','picture_choices','describe']

admin.site.register(Permission,PermissionAdmin)
admin.site.register(ArticleComment,ArticleCommentAdmin)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Picture,PictureAdmin)
admin.site.register([Category, Type, Notice,About,AboutType])