from django.db import models


class Article(models.Model):
    title = models.CharField(
        max_length=255,
        )

    text = models.CharField(
        max_length=1000,
        )

    decription = models.TextField(
        null=True,
        blank=True,
    )
    category = models.ForeignKey(
        'Category', 
        on_delete=models.SET_NULL,
        null=True,
    )

    def __str__(self):
        return "Статья: " + '"' + self.title + '"'
    # Reporter, on_delete=models.CASCADE 

class Category(models.Model):
    name = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
