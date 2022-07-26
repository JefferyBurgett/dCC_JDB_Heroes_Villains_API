from rest_framework import serializers
from .models import SuperType

class SuperTypeSerializer(serializers.ModelSerializer):
    class Meta:
        type = SuperType
        fields = ['super_type']
