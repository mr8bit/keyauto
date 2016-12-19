from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Image)
admin.site.register(Mark)
admin.site.register(Model)
admin.site.register(Seller)
admin.site.register(City)


class ImageInline(admin.TabularInline):
    model = Image
    extra = 0
    fields = ('image_tag',)
    readonly_fields = ('image_tag',)
    suit_classes = 'suit-tab suit-tab-images'


class ProductAdmin(admin.ModelAdmin):
    inlines = (ImageInline,)
    fieldsets = [
        ('Основная информация', {
            'classes': ('suit-tab', 'suit-tab-general',),
            'fields': [
                'url',  'model', 'year',
                'price', 'currency_type', 'run',
                'run_metric', 'stock','additional_info'
            ]
        }),
        (None, {
            'classes': ('suit-tab', 'suit-tab-characteristic',),
            'fields': [
                'horse_power', 'color', 'body_type', 'engine_type',
                'gear_type', 'transmission', 'steering_wheel', 'displacement'
            ]}),
        (None, {
            'classes': ('suit-tab', 'suit-tab-images',),
            'fields': []}),
    ]
    suit_form_tabs = (('general', 'Основные'),
                      ('characteristic', 'Характеристики'),
                      ('images', 'Изображения'),)


admin.site.register(Auto, ProductAdmin)
