from django.shortcuts import HttpResponse
import urllib.request as ur
import xmltodict
from .models import *
import requests
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile
from django.core.exceptions import ObjectDoesNotExist

import datetime
def update_auto(request):
    file = ur.urlopen('http://tradeins.ru/xml/yandex/285.new.xml    ')
    data = file.read()
    file.close()
    data = xmltodict.parse(data)
    list = data["auto-catalog"]["offers"]
    for auto in list['offer']:
        try:
            url = auto['url']
            car = Auto.objects.get(url=url)
            print("in base: "+ car.url)
        except ObjectDoesNotExist:
            try:
                mark = Mark.objects.get(name=auto['mark'])
                try:
                    model = Model.objects.get(name=auto['model'])
                except ObjectDoesNotExist:
                    model = Model.objects.create(name=auto['model'], mark=mark)
                    model.save()
                update_car(auto,  model)
            except ObjectDoesNotExist:
                mark = Mark.objects.create(name=auto['mark'])
                mark.save()
                try:
                    model = Model.objects.get(name=auto['model'])
                    update_car(auto,  model)
                except ObjectDoesNotExist:
                    model = Model.objects.create(name=auto['model'],mark=mark)
                    model.save()
                    update_car(auto, model)
    return HttpResponse("", content_type='application/json')


def update_car(auto,  model):
    try:
        seller = Seller.objects.get(seller=auto['seller'])
    except ObjectDoesNotExist:
        try:
            city = City.objects.get(name=auto['seller-city'])
        except ObjectDoesNotExist:
            city = City.objects.create(name=auto['seller-city'])
            city.save()
        seller = Seller.objects.create(city=city, seller=auto['seller'], phone=auto['seller-phone'])
        seller.save()
    car = Auto.objects.create(model=model,year=int(auto['year']), seller=seller, horse_power=int(auto['horse-power']))
    car.price = auto['price']
    car.url = auto['url']
    car.currency_type = auto['currency-type']
    car.run = auto['run']
    car.color = auto['color']
    car.body_type = auto['body-type']
    car.engine_type = auto['engine-type']
    car.run_metric = auto['run-metric']
    car.gear_type = auto['gear-type']
    car.transmission = auto['transmission']
    car.steering_wheel = auto['steering-wheel']
    car.displacement = auto['displacement']
    car.stock = auto['stock']
    car.additional_info = auto['additional-info']
    car.save()
    print ("update: " + car.url)
    if len(auto["image"]) > 1:
        for picture in auto["image"]:
            if len(picture) == 1:
                print("start download img" + str(datetime.datetime.now()))
                img = Image.objects.create(auto=car, url=auto["image"])
                img.save()
                print("end download img" + str(datetime.datetime.now()))
                break
            else:
                print("start download img" + str(datetime.datetime.now()))
                img = Image.objects.create(auto=car, url=picture)
                img.save()
                print("end download img" + str(datetime.datetime.now()))
