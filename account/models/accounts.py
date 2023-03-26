from django.contrib.auth.models import User
from django.db.models import *


class Account(Model):
    login = OneToOneField(User, null=True, blank=True, on_delete=SET_NULL, verbose_name='Войти')
    first_name = CharField('Имя', max_length=70)
    last_name = CharField('Фамилия', max_length=70)
    can_create = BooleanField('Возможность создавать тесты', default=False)

    def __str__(self):
        username = f'({self.login.username})' if self.login else ''
        return f'{self.first_name} {self.last_name}{username}'

    class Meta:
        db_table = 'accounts'
        verbose_name = 'Аккаунт'
        verbose_name_plural = 'Аккануты'
