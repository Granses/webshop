from django.db import models


class Theme(models.Model):

    name = models.CharField(max_length=100, unique=True, null=False)

    def __str__(self) -> str:
        return str(self.name)


class Article(models.Model):
    header = models.CharField(max_length=100, null=False)
    about = models.TextField(max_length=500, null=False)
    picture = models.FileField(upload_to='pictures/', null=False)
    author = models.CharField(max_length=100, null=False)
    publish = models.DateTimeField(null=False)
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.header)


class Comment(models.Model):

    username = models.CharField(max_length=100)
    comment = models.TextField(max_length=250,null=False)
    publish = models.DateTimeField(null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return str(self.username)