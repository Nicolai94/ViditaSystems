from drf_complete_autocomplete.serializers import WithAutocomplete
from rest_framework import serializers
from api.models import Image


class ImageSerializer(WithAutocomplete, serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['image']


class ImageDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


