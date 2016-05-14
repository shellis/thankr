from rest_framework import serializers
from thankr.moments.models import Moment

class MomentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Moment
        fields = ('id', 'text', 'title', 'category', 'rating')