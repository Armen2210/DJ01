from django.db import models

# Create your models here.
class News_post(models.Model):
    title = models.CharField('Название новости', max_length=100)
    short_description = models.CharField('Краткое описание новости', max_length=255)
    text = models.TextField('Полное описание новости')
    name = models.CharField('Имя автора', max_length=100)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

