from updater.models import *
from django.template.response import TemplateResponse


def main(request):
    context = {}
    return TemplateResponse(request, "main/base.html", context)


def technical_inspection(request):
    context = {}
    return TemplateResponse(request, "main/technical_inspection.html", context)


def seller(request):
    context = {}
    return TemplateResponse(request, "main/seller.html", context)


def new_auto(request):
    context = {}
    return TemplateResponse(request, "main/new_auto.html", context)
