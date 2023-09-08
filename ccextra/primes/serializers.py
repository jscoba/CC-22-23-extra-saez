from rest_framework import serializers
from .models import Prime

class PrimeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prime
        fields = '__all__'