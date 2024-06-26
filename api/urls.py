from django.urls import path
#from .views import Black_Coffer, Intensity, Country, Topics, Sector
#from .views import Likelihood, Relevance, End_Year, Start_Year
from api.views import *
urlpatterns = [
    
    path('blackcoffer/', Black_Coffer.as_view(), name='black_coffer'),
    path('intensity/', Intensity.as_view(), name='intensity'),
    path('likelihood/', Likelihood.as_view(), name='likelihood'),
    path('relevance/', Relevance.as_view(), name='relevance'),
    path('end_year/', End_Year.as_view(), name='end_year'),
    path('start_year/', Start_Year.as_view(), name='start_year'),
    
    path('topic/', Topics.as_view(), name='topic'),
    path('country/', Country.as_view(), name='country'),
    path('region/', Region.as_view(), name='region'),
    path('sector/', Sector.as_view(), name='sector'),

    path('pestle/', PestleDetail.as_view(), name='pestle'),
    path('source/', SourceDetail.as_view(), name='source'),

    path('detail/<int:id>/', DetailSearch.as_view(), name='region-detail'),
    
]