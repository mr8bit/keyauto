from django.shortcuts import render
from updater.models import *
from .serializers import *
from rest_framework import viewsets
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class MarkViewSet(viewsets.ModelViewSet):
    serializer_class = MarkSerializer
    queryset = Mark.objects.all()


class AutoViewSet(viewsets.ModelViewSet):
    serializer_class = AutoSerializer
    queryset = Auto.objects.all()


class SellerViewSet(viewsets.ModelViewSet):
    serializer_class = CitySeller
    queryset = City.objects.all()


class SnippetDetail(APIView):
    def get(self, request, pk, format=None):
        snippet = Auto.objects.filter(model=pk)
        serializer = AutoSerializer(snippet, context={'request': request}, many=True)
        return Response(serializer.data)
