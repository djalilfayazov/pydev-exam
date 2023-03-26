from django.db.models import Count
from django.shortcuts import render

from quiz.models import Category


def index_view(request):
    categories = Category.objects.all()

    context = {
        'title': 'Сайт викторин',
        'categories': categories,
    }
    return render(request, 'quiz/index.html', context)
