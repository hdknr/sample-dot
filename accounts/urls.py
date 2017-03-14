from django.conf.urls import url, include
from django.contrib.auth.views import login
from . import api

urlpatterns = [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/profile/$', api.profile, name='accounts_api_profile'),
    url(r'^api/now/$', api.now, name='accounts_api_now'),
    url(r'^login/', login, name='accounts_login',
        kwargs={'template_name': 'admin/login.html'}),
]
