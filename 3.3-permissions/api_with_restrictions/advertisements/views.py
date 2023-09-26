from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement
from advertisements.permissions import IsOwner
from advertisements.serializers import AdvertisementSerializer

from rest_framework.throttling import UserRateThrottle

class AdvertisementViewSet(ModelViewSet):
   queryset = Advertisement.objects.all()
   serializer_class = AdvertisementSerializer
   throttle_classes = [UserRateThrottle]
   filterset_class = AdvertisementFilter

   def get_permissions(self):
      """Получение прав для действий."""
      if self.action == "create":
         return [IsAuthenticated()]
      elif self.action in ["update", "partial_update", "destroy"]:
         return [IsAuthenticated(), IsOwner()]
      return []

