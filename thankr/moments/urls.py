from django.conf.urls import url

from thankr.moments.resources.views import MomentList, MomentDetail, Suggestion

urlpatterns = [
    url(r'^suggestion/', Suggestion.as_view()),
    url(r'^add/', MomentDetail.as_view()),
    url(r'^', MomentList.as_view())
]
