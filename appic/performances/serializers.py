from rest_framework import serializers
from performances.models import Performance

class PerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Performance
        fields = '__all__'
    