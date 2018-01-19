#! -*- coding:utf-8 -*-
from rest_framework import serializers
from .models import Article,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id','name', 'slug', 'created_time', 'last_modified_time')

class ArticleSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    category = CategorySerializer()
    class Meta:
        model = Article
        fields = ('id','title', 'body','created_time','last_modified_time','status','abstract','site','author','source','views','likes','category','type')

    # 待修改
    def create(self, validated_data):
        """响应 POST 请求"""
        # 自动为用户提交的 model 添加 owner
        validated_data['owner'] = self.context['request'].user
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """响应 PUT 请求"""
        instance.views = validated_data.get('views', instance.views)
        instance.likes = validated_data.get('likes', instance.likes)
        instance.save()
        return instance
