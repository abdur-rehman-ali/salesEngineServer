from rest_framework import viewsets
from .models import PseudoProfile
from .serializers import PseudoProfileSerializer

class PseudoProfileViewset(viewsets.ModelViewSet):
  queryset = PseudoProfile.objects.all()
  serializer_class = PseudoProfileSerializer
