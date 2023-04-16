from django.db.models import fields
from rest_framework import serializers
from .models import Basetable,Tags,Category

class BasetableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Basetable
        fields = ['basetable_id','id','name','photourls','status']

class TagsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tags
        fields = ('tags_id','t_name','t_id','basetable_id')
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('category_id','c_name','c_id','basetable_id')