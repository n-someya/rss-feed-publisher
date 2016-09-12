from django.db import models

# Create your models here.


class Feed(models.Model):
    "RSS Feed"
    id = models.TextField('ID', primary_key=True)
    link = models.TextField('link')
    title = models.TextField('タイトル')
    summary = models.TextField('サマリ')
    updated = models.DateTimeField('更新日時')

    def __str__(self):
        return self.id


