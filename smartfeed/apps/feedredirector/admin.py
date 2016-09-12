from django.contrib import admin
from smartfeed.apps.feedredirector.models import Feed

# Register your models here.


class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'summary', 'link', 'updated',)  # 一覧に出したい項目
    list_display_links = ('id', 'title',)  # 修正リンクでクリックできる項目
admin.site.register(Feed, FeedAdmin)


