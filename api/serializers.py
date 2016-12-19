from rest_framework import serializers
from updater.models import *


class ModelSerializer(serializers.ModelSerializer):
    count = serializers.ReadOnlyField(source='len')
    min_price = serializers.ReadOnlyField(source='price')

    class Meta:
        model = Model
        fields = ('id', 'name', 'image', 'count', 'min_price')


class MarkSerializer(serializers.ModelSerializer):
    models = ModelSerializer(read_only=True, many=True)

    class Meta:
        model = Mark
        fields = ('id', 'name', 'image', 'models')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id','url',)


class SellerSerializer(serializers.ModelSerializer):
    city = serializers.ReadOnlyField(source='get_city')

    class Meta:
        model = Seller
        fields = ('seller', 'city', 'phone', 'adress', 'image',)


class CitySeller(serializers.ModelSerializer):
    sellers = SellerSerializer(read_only=True, many=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'sellers')


class AutoSerializer(serializers.ModelSerializer):
    model = ModelSerializer(read_only=True, many=False)
    images = ImageSerializer(many=True, read_only=True)
    seller = SellerSerializer(many=False, read_only=True)
    s_price = serializers.ReadOnlyField(source='str_price')
    mark = serializers.ReadOnlyField(source='get_mark')
    tth = serializers.ReadOnlyField(source='get_tth')
    seller = SellerSerializer(many=False, read_only=True)

    class Meta:
        model = Auto
        fields = ('id',
                  'model',
                  'mark',
                  'year',
                  'seller',
                  's_price',
                  'price',
                  'currency_type',
                  'run',
                  'run_metric',
                  'horse_power',
                  'color',
                  'body_type',
                  'seller',
                  'engine_type',
                  'gear_type',
                  'transmission',
                  'steering_wheel',
                  'displacement',
                  'stock',
                  'tth',
                  'images')
