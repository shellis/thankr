from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.renderers import TemplateHTMLRenderer
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from thankr.moments.resources.serializers import MomentSerializer
from thankr.moments.models import Moment, Category
from thankr.analytics.categorizer import categorize

from django.db.models import Max
from django.db.models import Count

class MomentDetail(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'add_moment.html'

	def get(self, request):
		serializer = MomentSerializer()
		return Response({'serializer': serializer})

	def post(self, request):
		serializer = MomentSerializer(data=request.data)
		if not serializer.is_valid():
			return Response({'serializer': serializer})
		suggested_category = categorize(serializer.validated_data['text'])
		try:
			cat_db = Category.objects.get(name__exact=suggested_category)
			print("Category most matched:", cat_db.name)
			suggested_category_id = cat_db.id
		except ObjectDoesNotExist:
			suggested_category_id = None
		serializer.save(user_id=request.user.id, suggested_category_id=suggested_category_id)
		return HttpResponseRedirect('/moments/')

class MomentList(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'moments.html'

	def get(self, request):
		moments = Moment.objects.filter(user_id=request.user.id)
		moments_serializer = MomentSerializer(moments, many=True)
		return Response({'moments': moments_serializer.data})


class Suggestion(APIView):
	permission_classes = (permissions.IsAuthenticated,)
	renderer_classes = [TemplateHTMLRenderer]
	template_name = 'suggestion.html'

	def get(self, request):
		maxTuple = Moment.objects.filter(user_id=request.user.id).values("suggested_category").annotate(total=Count("suggested_category")).order_by("total")[0]
		maxSuggestedCategory = maxTuple["suggested_category"]
		return Response({'topCategory': maxSuggestedCategory})	






