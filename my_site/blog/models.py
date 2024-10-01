from django.core import validators
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator
from django.urls import reverse
from django.utils.text import slugify

class Tag(models.Model):
    caption= models.CharField(max_length=20)
    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    e_mail = models.EmailField(max_length=30)
    def __str__(self):
        return f"{self.first_name}"
class Post(models.Model):
    title = models.CharField(max_length=150)
    excert = models.CharField(max_length=200)
    Imagename = models.CharField(max_length=30)
    date  = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True)
    slug = models.SlugField(default="", blank=True, null=False, db_index=True)

    def get_absolute_url(self):
        return reverse("post-detail", args=[self.slug])

    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name="posts")
    tag = models.ManyToManyField(Tag)
    def __str__(self):
        return f"{self.title} ({self.date})"