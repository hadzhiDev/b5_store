from django.db import models


class Category(models.Model):
    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

    name = models.CharField('название', max_length=250, unique=True)

    def __str__(self):
        return f'{self.name}'


class Tag(models.Model):
    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    name = models.CharField('название', max_length=255)

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    class Meta:
        verbose_name = 'Продукта'
        verbose_name_plural = 'Продукты'

    name = models.CharField('название', max_length=100)
    description = models.CharField('описание', max_length=255, help_text='Просто описание')
    content = models.TextField('контент')
    category = models.ForeignKey('store.Category', models.PROTECT, verbose_name='категория',
                                 help_text='Выберите категорию')
    tags = models.ManyToManyField('store.Tag', verbose_name='теги')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2, default=0.0)
    quantity = models.PositiveIntegerField('количество', default=1)

    def __str__(self):
        return f'{self.name} - {self.price}'



