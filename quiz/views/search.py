from django.views.generic import ListView
from quiz.models.categories import Category
from django.db.models import Q
from django.shortcuts import render


def search(request):
     query = request.GET.get("category")
     object_list = Category.objects.filter(
          Q(title__icontains=query)
     )

     return render(
          request, 'quiz/search.html',
          {
               'title': f'Поиск по запросу "{query}"',
               'objects': object_list
          }
     )


'''class Search(ListView):
     model = Category
     template_name = 'quiz/search.html'

     def get_queryset(self):
          query = self.request.GET.get("category")
          object_list = Category.objects.filter(
               Q(title__icontains=query)
          )

          return object_list
'''