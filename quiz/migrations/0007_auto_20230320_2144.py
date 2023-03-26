# Generated by Django 3.2.10 on 2023-03-20 16:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0006_auto_20230313_1518'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='full_text',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='created',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='modified',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quiz.category', verbose_name='Категория'),
        ),
    ]
