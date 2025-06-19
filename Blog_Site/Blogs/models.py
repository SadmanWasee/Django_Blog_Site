from django.db import models

# Create your models here.
class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=250, unique=True)

    class Meta: 
        verbose_name_plural = "Authors"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Tag(models.Model):
    caption = models.CharField(max_length=75)

    def __str__(self):
        return f"{self.caption}"
    
class Post(models.Model):
    title = models.CharField(max_length=150)
    excerpt = models.CharField(max_length=255)
    image_name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add = True)
    slug = models.SlugField(default="", null=False, db_index = True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    tag = models.ManyToManyField(Tag, null=True)

    def __str__(self):
        return f"{self.title}"