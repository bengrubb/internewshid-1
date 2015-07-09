from __future__ import unicode_literals, absolute_import
from rest_framework import serializers

from data_layer.models import Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item