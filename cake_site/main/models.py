from django.db import models


class Cake(models.Model):
    name = models.CharField('Название', max_length=50)
    anons = models.TextField('Описание')
    price = models.PositiveSmallIntegerField('Цена')
    #image = models.ImageField('Фото', upload_to='images/')

    def __str__(self):
        return self.name


class Feedback(models.Model):
    name_u = models.CharField('Имя', max_length=50)
    review_u = models.TextField('Отзыв')

    def __str__(self):
        return self.name_u