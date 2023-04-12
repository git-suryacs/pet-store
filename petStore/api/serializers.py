from django.db.models import fields
from rest_framework import serializers
from .models import Basetable,Tags,Category

class BasetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basetable
        fields = ('basetable_id','photourls','name','id','status')

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('tags_id','name','id,','basetable_id')
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id','name','id','basetable_id')