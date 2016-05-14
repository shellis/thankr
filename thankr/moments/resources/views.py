from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.renderers import TemplateHTMLRenderer

from thankr.moments.resources.serializers import MomentSerializer
from thankr.moments.models import Moment

class MomentsResource(APIView):
	permission_classes = (permissions.IsAuthenticated,)

	def get(self, request):
		moments = Moment.objects.filter(user_id=request.user.id)

		moments_serializer = MomentSerializer(moments, many=True)
		return Response(moments_serializer.data, status=status.HTTP_200_OK)


	def post(self, request):
		user_id = request.user.id
		try:
			title = request.data['title']
			text = request.data['text']
		except KeyError:
			return Response("parse error", status=status.HTTP_400_BAD_REQUEST)

		category_id = request.data['category_id'] if 'category_id' in request.data else None
		rating = request.data['rating'] if 'rating' in request.data else None

		moment = Moment(user_id = user_id,
						title = title,
						text = text,
						category_id = category_id,
						rating = rating)
		moment.save()
		return Response(MomentSerializer(moment).data, status=status.HTTP_200_OK)


class MomentList(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'moments.html'

	def get(self, request):
		moments = Moment.objects.filter(user_id=request.user.id)
		moments_serializer = MomentSerializer(moments, many=True)
		return Response({'moments': moments_serializer.data})