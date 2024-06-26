from django.shortcuts import render
from api.models import BlackCoffer
from .serializers import BlackCofferSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Count
from rest_framework import status
 
class Black_Coffer(APIView):
    def get(self, request, format=None):
        queryset = BlackCoffer.objects.all()
        serializer = BlackCofferSerializer(queryset, many=True)
        return Response(serializer.data)
    
# this class for finding detail information for any of specific id 
class DetailSearch(APIView):
    def get(self, request, id):
        queryset = BlackCoffer.objects.filter(pk=id).values()
        return Response(queryset)
    
class Intensity(APIView):
    def get(self, request):
        intensity = BlackCoffer.objects.values('intensity').annotate(count=Count('id'))
        return Response(intensity)
    
class Likelihood(APIView):
    def get(self, request):
        likelihood = BlackCoffer.objects.values('likelihood').annotate(count=Count('id'))
        return Response(likelihood)
    
class Relevance(APIView):
    def get(self, request):
        relevance = BlackCoffer.objects.values('relevance').annotate(count=Count('id'))
        return Response(relevance)
class End_Year(APIView):
    def get(self, request):
        end_year = BlackCoffer.objects.values('end_year').annotate(count=Count('id'))
        
        return Response(end_year)
class Start_Year(APIView):
    def get(self, request):
        start_year = BlackCoffer.objects.values('start_year').annotate(count=Count('id'))
        return Response(start_year)
    
class Country(APIView):
    def get(self, request):
        country = BlackCoffer.objects.values('country').annotate(count=Count('id'))
        return Response(country)
    
class Region(APIView):
    def get(self, request):
        region = BlackCoffer.objects.values('region').annotate(count=Count('id'))
        return Response(region)

class Topics(APIView):
    def get(self, request):
        topic = BlackCoffer.objects.values('topic').annotate(count=Count('id'))
        return Response(topic)
    
class Sector(APIView):
    def get(self, request):
        sector = BlackCoffer.objects.values('sector').annotate(count=Count('id'))
        return Response(sector)
    

class SourceDetail(APIView):
    def get(self, request):
        sector = BlackCoffer.objects.values('source').annotate(count=Count('id'))
        return Response(sector)

class PestleDetail(APIView):
    def get(self, request):
        pestle = BlackCoffer.objects.values('pestle').annotate(count=Count('id'))
        return Response(pestle)

