# Generated by Django 4.0.4 on 2022-06-02 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_u', models.CharField(max_length=50, verbose_name='Имя')),
                ('review_u', models.TextField(verbose_name='Отзыв')),
            ],
        ),
    ]