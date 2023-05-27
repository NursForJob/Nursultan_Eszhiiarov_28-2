from django.db import models

# Create your models here.
# python manage.py makemigrations - создает миграцию
# python manage.py migrate - запускаем миграцию


class Post(models.Model):                               # создаем модели models.Model, без них это просто класс
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=30)
    description = models.TextField()
    rate = models.FloatField(default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title                               # чтоб в панели были видны названия заголовок