from django.db import models


class Wear(models.Model):
    """Abstract class for all type of wears: shoes, hats, shirts and etc."""

    title = models.CharField(max_length=128, verbose_name='Название товара')
    price = models.IntegerField(default=0, verbose_name='Цена товара')
    size = models.IntegerField(default=48, verbose_name='Размер товара')
    composition = models.TextField(verbose_name='Состав')
    collection = models.TextField(verbose_name='Коллекция')
    color = models.CharField(max_length=256, null=True, blank=True)
    category = models.ForeignKey('Categories', on_delete=models.SET_NULL, null=True)

    class Meta:
        abstract = True


class OuterWear(Wear):

    def __str__(self):
        return f'{self.title}'


class Shoes(Wear):
    insole_material = models.CharField(max_length=32, verbose_name='Материал стельки')

    def __str__(self):
        return f'{self.title}'


class TShirts(Wear, models.Model):

    def __str__(self):
        return f'{self.title}'
