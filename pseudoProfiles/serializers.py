from rest_framework import serializers
from .models import PseudoProfile

class PseudoProfileSerializer(serializers.ModelSerializer):
  created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
  updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

  class Meta:
    model = PseudoProfile
    fields = '__all__'

