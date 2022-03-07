from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title
