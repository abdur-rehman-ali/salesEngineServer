from rest_framework import viewsets
from .models import JobSource
from .serializers import JobSourceSerializer

class JobSourceViewSet(viewsets.ModelViewSet):
  queryset = JobSource.objects.all()
  serializer_class = JobSourceSerializer
