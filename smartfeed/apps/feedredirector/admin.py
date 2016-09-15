from django.contrib import admin
from smartfeed.apps.feedredirector.models import Feed, User, Article, SubscribedFeed, UserArticleCount

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)  # 一覧に出したい項目
    list_display_links = ('name',)  # 修正リンクでクリックできる項目
admin.site.register(User, UserAdmin)


class FeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'url',)  # 一覧に出したい項目
    list_display_links = ('id', 'url',)  # 修正リンクでクリックできる項目
admin.site.register(Feed, FeedAdmin)


class SubscribedFeedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'feed',)  # 一覧に出したい項目
    list_display_links = ('id', 'user', 'feed')  # 修正リンクでクリックできる項目
admin.site.register(SubscribedFeed, SubscribedFeedAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id', 'link', 'title', 'summary', 'updated')
    list_display_links = ('link', 'title', 'summary', 'updated')  # 修正リンクでクリックできる項目
admin.site.register(Article, ArticleAdmin)


class UserArticleCountAdmin(admin.ModelAdmin):
    list_display = ('id', 'article', 'user', 'count')
    list_display_links = ('id',)  # 修正リンクでクリックできる項目
admin.site.register(UserArticleCount, UserArticleCountAdmin)
