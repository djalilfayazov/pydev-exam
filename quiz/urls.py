from django.urls import path
from quiz.views import *

urlpatterns = [
    path('', index_view, name='index'),

    path('new-category/', create_category, name='createcat'),
    path('new-test/', create_test, name='createtest'),
    path('new-question/', create_qs, name='createqs'),

    #path('new-test/', CreateTest.as_view(), name='createtest'),
    #path('new-question/', CreateQs.as_view(), name='createqs'),
    #path('new-category/', CreateCategory.as_view(), name='createcat'),

    #path('search', Search.as_view(), name='search'),
    path('search', search, name='search'),

    path('<slug:category_slug>/', category_view, name='category'),
    path('<slug:category_slug>/<slug:quiz_slug>/', quiz_view, name='quiz'),
]
