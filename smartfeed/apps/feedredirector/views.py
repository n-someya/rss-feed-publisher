from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist

from smartfeed.apps.feedredirector.models import Article, User, UserArticleCount

# Create your views here.

def show(request, article_id, user_id):
    """SHOW"""
    article = get_object_or_404(Article, pk=article_id)
    user = get_object_or_404(User, pk=user_id)
    try:
        user_art_count = UserArticleCount.objects.get(user=user, article=article)
        user_art_count.count += 1
    except ObjectDoesNotExist:
        user_art_count = UserArticleCount(user=user, article=article)

    user_art_count.save()
    return redirect(article.link)
