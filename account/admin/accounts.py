from django.contrib import admin
from account.models import *


@admin.register(Account)
class AccountModelAdmin(admin.ModelAdmin):
    pass
