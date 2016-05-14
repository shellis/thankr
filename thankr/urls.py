"""thankr URL Configuration
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView

from thankr.accounts import views as account_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', account_views.user_login, name='login'),
    url(r'^register/', account_views.register),
    url(r'^logout/', "thankr.accounts.views.user_logout", name='logout'),
    url(r'^moments/', include('thankr.moments.urls')),
    url(r'^', TemplateView.as_view(template_name='index.html'))
]
