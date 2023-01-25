from django.db import models


class Newss(models.Model):
    title = models.CharField('Название', max_length=30, default='ничего')
    intro = models.CharField("О чем", max_length=200)
    text = models.TextField('Новость')
    date = models.DateTimeField('Дата')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
