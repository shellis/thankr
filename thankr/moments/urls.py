from django.conf.urls import url
from thankr.moments.resources.views import MomentList

urlpatterns = [

    #url(r'^api/', MomentsResource.as_view()),
    url(r'^', MomentList.as_view()),
]
