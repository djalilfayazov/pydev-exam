from django.db.models import *
from quiz.models import *


class Question(Model):
    quiz = ForeignKey(Quiz, on_delete=CASCADE, verbose_name='Викторина')
    question = CharField('Текст вопроса', max_length=512)

    def __str__(self):
        return self.question[:50]

    class Meta:
        db_table = 'questions'
        verbose_name = 'Вопрос виктоины'
        verbose_name_plural = 'Вопросы викторин'
