from django.db.models import *
from django.urls import reverse

from account.models import *
from quiz.models import *


class Quiz(Model):
    author = ForeignKey(Account, on_delete=PROTECT, verbose_name='Автор')
    title = CharField('Название', max_length=512)
    slug = SlugField('URL', unique=False)
    
    is_public = BooleanField('Отображение', default=True)
    category = ForeignKey('Category', on_delete=PROTECT, verbose_name='Категория')


    def __str__(self):
        return self.title

    class Meta:
        db_table = 'quiz'
        verbose_name = 'Викторина'
        verbose_name_plural = 'Викторины'
        unique_together = ('slug', 'category')
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse(
            'quiz',
            kwargs={
                'quiz_slug': self.slug,
                'category_slug': self.category.slug,
            }
        )
