from rest_framework import serializers
from thankr.moments.models import Category, Moment

class CategoryField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return instance.name

class MomentSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()
    class Meta:
        model = Moment
        fields = ('id', 'date', 'title', 'text', 'rating', 'category_name')
        read_only_fields = ('id',)

    def get_category_name(self, obj):
        return obj.category.name
