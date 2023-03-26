from django.db.models import *
from django.urls import reverse


class Category(Model):
    title = CharField('Категория',max_length=512)
    slug = SlugField('URL',unique=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'categories'
        verbose_name = 'Рубрика'
        verbose_name_plural = 'Рубрики'
        ordering = ('id',)

    def get_absolute_url(self):
        return reverse(
            'category',
            kwargs={
                'category_slug': self.slug,
            }
        )
