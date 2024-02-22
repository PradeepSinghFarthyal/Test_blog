from django.db import models
import uuid
# Create your models here.


class Category(models.Model):
    category_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    category_name = models.CharField(max_length=255, null=False)
    # create_at


class Tags(models.Model):
    tage_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tags_name = models.CharField(max_length=255, null=False)


class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    blog_name = models.CharField(max_length=255, null=False)
    blog_category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Blog_tags(models.Model):
    blod_tag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    tags_details = models.ForeignKey(Tags, on_delete=models.CASCADE)
    blog_details = models.ForeignKey(Blog, on_delete=models.CASCADE)