from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    name = models.TextField('name', null=True)

    def __str__(self):
        return str(self.id) + ":" + self.name


class Feed(models.Model):
    "RSS Feed"
    url = models.TextField('url', null=True)

    def __str__(self):
        return str(self.id)


class SubscribedFeed(models.Model):
    "Subscribed RSS Feed"
    user = models.ForeignKey(User, null=True)
    feed = models.ForeignKey(Feed, null=True)

    def __str__(self):
        return str(self.id)


class Article(models.Model):
    feed = models.ForeignKey(Feed, null=True)
    link = models.TextField('link', null=True)
    title = models.TextField('タイトル', null=True)
    summary = models.TextField('サマリ', null=True)
    updated = models.DateTimeField('更新日時', default=timezone.now)

    def __str__(self):
        return str(self.id)


class UserArticleCount(models.Model):
    article = models.ForeignKey(Article, null=True)
    user = models.ForeignKey(User, null=True)
    count = models.IntegerField('count', default=1)

    def __str__(self):
        return str(self.id)


    class Meta:
        unique_together = ('article', 'user', )


