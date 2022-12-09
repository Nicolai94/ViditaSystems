from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from api.models import Image
from api.serializers import ImageSerializer, ImageDetailsSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet


class ImagesViewSet(ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['geo_location', 'description', 'name']
    search_fields = ['name']


class ImagesUploadViewSet(ModelViewSet):
    queryset = Image.objects.none()
    serializer_class = ImageDetailsSerializer


class ImagesDetailsViewSet(ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageDetailsSerializer

    def get_queryset(self, *args, **kwargs):
        qs = super().get_queryset(*args, **kwargs)
        id = self.kwargs['pk']
        return qs.filter(id=id)


