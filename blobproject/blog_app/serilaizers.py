from rest_framework import serializers
from .models import Blog, Category, Tags

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = '__all__'

class BlogDetailSerializer(serializers.ModelSerializer):
    blog_category = CategorySerializer()
    tags_details = TagsSerializer(many=True)

    class Meta:
        model = Blog
        fields = '__all__'

class BlogSubmitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['blog_name', 'blog_category']  # Include fields that you want to accept in the POST request