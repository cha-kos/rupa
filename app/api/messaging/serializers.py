from rest_framework import serializers
from .fields import HTMLToPlainTextField


class EmailSerializer(serializers.Serializer):
    to_email = serializers.EmailField()
    to_name = serializers.CharField()
    from_email = serializers.EmailField()
    from_name = serializers.CharField()
    subject = serializers.CharField()
    body = HTMLToPlainTextField()
