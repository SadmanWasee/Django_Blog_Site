from django.db import models

# Create your models here.

class Tag(models.Model):
    caption = models.CharField(max_length=75)

    def __str__(self):
        return f"{self.caption}"
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=255)
    image_name = models.FileField()
    date = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(default="", null=False, db_index = True)
    content = models.TextField()
    author = models.CharField(max_length=150)
    tag = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return f"{self.title}"