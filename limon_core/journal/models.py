from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Категории публикаций'
        verbose_name = 'Категории публикации'

    def __str__(self):
        return self.title




class Hashtag(models.Model):
    title = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Хэштеги'
        verbose_name = 'Хэштег'


    def __str__(self):
        return self.title





class PublicationStatistic(models.Model):

    total_views_count = models.PositiveIntegerField()
    total_likes_count = models.PositiveIntegerField()



"""
id  |  total_views_count  |  total_likes_count|
-----------------------------------------------
1   |     5000            |  100              |
"""


"""
id  |  title                |   statistic_id |
--------------------------------------------
 1  | прошел чемпионат Азии |   1            |
"""


class Publication(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    hashtags = models.ManyToManyField(Hashtag) # Многие ко многим!
    statistic = models.OneToOneField(PublicationStatistic, on_delete=models.SET_NULL()),  # Один ко многим!
    topic = models.CharField(verbose_name= 'Названия', max_length=255, )
    description = models.TextField(verbose_name='Описания',)
    image = models.ImageField(verbose_name='Изображения', )
    read_time = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural = 'Публикации'
        verbose_name = 'Публикации'

