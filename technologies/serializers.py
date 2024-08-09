from rest_framework import serializers
from .models import Technology

class TechnologySerializer(serializers.ModelSerializer):
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
  updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

  class Meta:
    model = Technology
    fields = ['id', 'name', 'created_at', 'updated_at']
