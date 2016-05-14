from django.conf.urls import url

from thankr.moments.resources.views import MomentList, MomentDetail

urlpatterns = [
    url(r'^add/', MomentDetail.as_view()),
    url(r'^', MomentList.as_view()),
]
