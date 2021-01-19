from rest_framework.viewsets import ModelViewSet
from appinfo.models import SystemList, SubSystemList
from appinfo.serializers import SystemListSerializer, SubSystemListSerializer

from django_filters import rest_framework as filters


# Create your views here.

class SystemListViewSet(ModelViewSet):
    queryset = SystemList.objects.all()
    serializer_class = SystemListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('app_short', 'dev_group', 'level', 'status')


class SubSystemListViewSet(ModelViewSet):
    queryset = SubSystemList.objects.all()
    serializer_class = SubSystemListSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filter_fields = ('subapp_short', 'app_short', 'dev_language', 'frame')
