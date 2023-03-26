from django.db.models import *
from quiz.models import Question


class Answer(Model):
    answer = CharField('Ответ', max_length=512)
    is_correct = BooleanField('Правильный', default=False)
    question = ForeignKey(Question, on_delete=CASCADE, verbose_name='Выбор вопроса')

    def __str__(self):
        return self.answer

    class Meta:
        db_table = 'answers'
        verbose_name = 'Ответ к вопросу'
        verbose_name_plural = 'Ответы к вопросам'

