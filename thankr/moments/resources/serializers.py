from rest_framework import serializers
from thankr.moments.models import Category, Moment

class CategoryField(serializers.PrimaryKeyRelatedField):
    def display_value(self, instance):
        return instance.name

class MomentSerializer(serializers.ModelSerializer):
    category = CategoryField(queryset=Category.objects.all())
    class Meta:
        model = Moment
        fields = ('id', 'date', 'title', 'text', 'category', 'rating')
        read_only_fields = ('id', 'suggested_category')
