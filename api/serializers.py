
from rest_framework import serializers
from api.models import BlackCoffer 

class BlackCofferSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlackCoffer 
        fields = '__all__'
    
    