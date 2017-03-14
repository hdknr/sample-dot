from django.conf.urls import url, include
from django.contrib.auth.views import login
from .views import profile

urlpatterns = [
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/profile/$', profile, name='accounts_profile'),
    url(r'^login/', login, name='accounts_login',
        kwargs={'template_name': 'admin/login.html'}),
]
