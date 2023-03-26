from django.contrib import admin
from quiz.models.answers import Answer


class AnswerTabularInline(admin.TabularInline):
    model = Answer
    min_num = 2
    extra = 0
