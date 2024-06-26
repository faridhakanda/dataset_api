from django.db import models

# Create your models here.
from django.db import models

class BlackCoffer(models.Model):
    
    end_year = models.CharField(max_length=100, blank=True, null=True)
    #end_year = models.IntegerField(null=True, blank=True)
    intensity = models.IntegerField(null=True, blank=True)
    sector = models.CharField(max_length=255, null=True, blank=True)
    topic = models.CharField(max_length=255, null=True, blank=True)
    insight = models.TextField(null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    region = models.CharField(max_length=255, null=True, blank=True)
    start_year = models.CharField(max_length=100, blank=True, null=True)
    #start_year = models.IntegerField(null=True, blank=True)
    impact = models.TextField(blank=True, null=True)
    added = models.DateTimeField(blank=True, null=True)
    published = models.DateTimeField(blank=True, null=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    relevance = models.IntegerField(null=True, blank=True)
    pestle = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
    title = models.TextField(null=True, blank=True)
    likelihood = models.IntegerField(null=True, blank=True)

   
    def __str__(self):
        return self.title
    