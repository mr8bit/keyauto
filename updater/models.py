from django.db import models
import locale

locale.setlocale(locale.LC_ALL, '')


class Mark(models.Model):
    name = models.CharField(max_length=400, verbose_name="Наиминование")
    image = models.ImageField(max_length=300, verbose_name="Логотип марки", default='', blank=True)

    def __str__(self):
        return self.name


class Model(models.Model):
    name = models.CharField(max_length=300, verbose_name="Наиминование")
    mark = models.ForeignKey("Mark", related_name='models', verbose_name="Марка", blank=True, on_delete=models.CASCADE)
    image = models.ImageField(max_length=300, verbose_name="Изображение модели", default='', blank=True)

    def len(self):
        return len(Auto.objects.filter(model=self))

    def price(self):
        x = int(Auto.objects.filter(model=self).aggregate(models.Min('price'))['price__min'])
        return str(locale.format('%d', x, grouping=True))

    def __str__(self):
        return self.name


class Auto(models.Model):
    url = models.CharField(max_length=400, verbose_name='Url', default='')
    model = models.ForeignKey("Model", verbose_name="Модель", blank=True, related_name='autos',
                              on_delete=models.CASCADE)
    year = models.IntegerField(verbose_name="Год", blank=True)
    price = models.CharField(max_length=400, verbose_name="Цена", blank=True)
    currency_type = models.CharField(max_length=400, verbose_name="Валюта", blank=True)
    seller = models.ForeignKey('Seller', verbose_name="Диллерский центр", blank=True, null=True)
    run = models.CharField(max_length=400, verbose_name="Пробег", blank=True)
    run_metric = models.CharField(max_length=400, verbose_name="Еденица пробега", blank=True)
    horse_power = models.IntegerField(verbose_name="Лошадинные силы", blank=True)
    color = models.CharField(max_length=400, verbose_name="Цвет", blank=True)
    body_type = models.CharField(max_length=400, verbose_name="Тип кузова", blank=True)
    engine_type = models.CharField(max_length=400, verbose_name="Тип двигателя", blank=True)
    gear_type = models.CharField(max_length=400, verbose_name="Привод", blank=True)
    transmission = models.CharField(max_length=400, verbose_name="Трансмисия", blank=True)
    steering_wheel = models.CharField(max_length=400, verbose_name="Руль", blank=True)
    displacement = models.CharField(max_length=400, verbose_name="Объем двигателя", blank=True)
    stock = models.CharField(max_length=400, verbose_name="Статус", blank=True)
    additional_info = models.TextField(verbose_name="Описание", blank=True, null=True)

    def __str__(self):
        return self.model.name

    def str_price(self):
        return str(locale.format('%d', int(self.price), grouping=True))

    def get_mark(self):
        return self.model.mark.name

    def get_tth(self):
        if self.additional_info:
            x = self.additional_info.split(':')
            return x[1].split(',')



class Image(models.Model):
    auto = models.ForeignKey("Auto", related_name="images")
    url = models.CharField(verbose_name="Изображение", max_length=4000,blank=True, null=True )

    def image_tag(self):
        return u'<a href="%s"><img src="%s" width="200"/></a>' % (self.url, self.url)

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True

    def __str__(self):
        return self.auto.model.name

    def get_url(self):
        return self.url


class Seller(models.Model):
    seller = models.CharField(max_length=500, verbose_name="Диллерский центр", blank=True, null=True)
    city = models.ForeignKey("City", verbose_name="Город", blank=True, null=True, related_name='sellers')
    phone = models.CharField(max_length=400, verbose_name="Телефон", blank=True, null=True)
    adress = models.CharField(max_length=400, verbose_name="Адресс", blank=True, null=True)
    image = models.ImageField(upload_to='seller/', verbose_name="Изображение", blank=True, null=True)

    def __str__(self):
        return self.seller

    def get_city(self):
        return self.city.name


class City(models.Model):
    name = models.CharField(max_length=400, verbose_name="Город", blank=True, null=True)

    def __str__(self):
        return self.name
