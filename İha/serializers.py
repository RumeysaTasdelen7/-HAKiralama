from rest_framework import serializers
from .models import İHA

class İHASerializer(serializers.ModelSerializer):
    class Meta:
        model = İHA
        fields = '__all__'
