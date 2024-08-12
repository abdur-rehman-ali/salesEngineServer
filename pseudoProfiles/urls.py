from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PseudoProfileViewset

router = DefaultRouter()
router.register(r'', PseudoProfileViewset)

urlpatterns = [
  path('', include(router.urls))
]
