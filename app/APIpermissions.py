# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        """针对每一次请求的权限检查"""
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        if request.user.is_staff:
            return True
        else:
            return request.method in permissions.SAFE_METHODS


    # def has_object_permission(self, request, view, obj):
    #     """针对数据库条目的权限检查，返回 True 表示允许"""
    #     # 允许访问只读方法
    #     if request.method in permissions.SAFE_METHODS:
    #         return True
    #
    #     # 非安全方法需要检查用户是否是 owner
    #     return obj.owner == request.user
