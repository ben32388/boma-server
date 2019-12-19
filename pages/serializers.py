from rest_framework import serializers

from .models import Page
from taggit_serializer.serializers import (TagListSerializerField, TaggitSerializer)

class PageSerializer(serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Page
        fields = '__all__'
        read_only_fields = ['user']
    
    def create(self, validated_data):
        tags = validated_data.pop('tags')
        instance = super(PageSerializer, self).create(validated_data)
        instance.tags.set(*tags)
        return instance