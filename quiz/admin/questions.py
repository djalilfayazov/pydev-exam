from django.contrib import admin
from quiz.admin.answers import AnswerTabularInline
from quiz.models import Question


@admin.register(Question)
class QuestionModelAdmin(admin.ModelAdmin):
    inlines = (
        AnswerTabularInline,
    )
    list_display = ('id', 'quiz', 'question')
    list_display_links = ('id', 'quiz')
    ordering = ('id',)
