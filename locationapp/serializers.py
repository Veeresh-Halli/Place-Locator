from rest_framework import serializers

class PlaceSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=200, required=True)
    description = serializers.CharField(required=True)
    latitude = serializers.FloatField(required=True)
    longitude = serializers.FloatField(required=True)