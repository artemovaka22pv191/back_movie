from django.contrib.auth.models import User
from django.db import models

class Genre(models.Model):
    name = models.CharField("Жанр", max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Жанр"
        verbose_name_plural = "Жанры"


class RaitingStar(models.Model):
    status = models.CharField("Статус", max_length=30, default='')
    value = models.IntegerField("Значение", default=0)

    def __str__(self):
        return f"{self.value}_{self.status}"

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"


class Movie(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField("Название", max_length=255)
    description = models.TextField("Описание")
    poster = models.ImageField("Постер", upload_to="pictures/")
    genres = models.ManyToManyField(Genre, verbose_name="жанры")
    user = models.ForeignKey(User, verbose_name="Пользователь", default=1, on_delete=models.SET_DEFAULT)
    mark = models.ForeignKey(RaitingStar, verbose_name="Оценка", default=1, on_delete=models.SET_DEFAULT)
    opinion = models.TextField("Мнение автора", default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Аниме"
        verbose_name_plural = "Аниме"


class Raiting(models.Model):
    ip = models.CharField(max_length=15)
    star = models.ForeignKey(RaitingStar, on_delete=models.CASCADE, verbose_name="Звезда")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Аниме")

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):
    name = models.CharField("Имя", max_length=100, null=False)
    text = models.TextField("Сообщение", max_length=10000, null = False)
    parent = models.ForeignKey(
        'self', on_delete=models.SET_NULL, verbose_name="Родитель", blank=True, null=True
    )
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, verbose_name="Аниме")
    children = models.ManyToManyField(
        'self', verbose_name="Дети", blank=True, null=True
    )
    date = models.DateTimeField(null=True, auto_now_add=True)
    #star = models.ForeignKey(RaitingStar, on_delete=models.CASCADE, verbose_name="Звезда")

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
