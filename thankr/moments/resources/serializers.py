from rest_framework import serializers
from thankr.moments.models import Moment

class MomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moment
        fields = ('id', 'date', 'text', 'title', 'category', 'rating')