from rest_framework import serializers
from mainapp.models import Ideas


class IdeasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ideas
        fields = ('id', 'name', 'idea')