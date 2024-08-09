from rest_framework import serializers
from .models import Technology

class TechnologySerializer(serializers.ModelSerializer):
  class Meta:
    model = Technology
    fields = ['id', 'name', 'created_at', 'updated_at']
