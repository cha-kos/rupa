from rest_framework import serializers
from .utils import parse_html


class HTMLToPlainTextField(serializers.Field):
    def to_internal_value(self, value):
        return parse_html(value)
