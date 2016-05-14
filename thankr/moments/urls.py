from django.conf.urls import url
from thankr.moments.resources.views import MomentsResource

urlpatterns = [

    url(r'^$', MomentsResource.as_view()),
]
