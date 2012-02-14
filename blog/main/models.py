from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']


class Comment(models.Model):
    article = models.ForeignKey('Article', related_name='comments')
    text = models.TextField()
