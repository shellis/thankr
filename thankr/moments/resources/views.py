from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from thankr.moments.resources.serializers import MomentSerializer
from thankr.moments.models import Moment

class MomentsResource(APIView):
	#permission_classes = (permissions.IsAuthenticated,)

	def get(self, request):
		moments = Moment.objects.filter(user_id=1)

		moments_serializer = MomentSerializer(moments, many=True)
		return Response(moments_serializer.data, status=status.HTTP_200_OK)