from django.db.models import fields
from rest_framework import serializers
from .models import Pet

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id','category','name','photoUrls','tags','status')
