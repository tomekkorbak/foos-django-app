from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^foos/(?P<slug>\S*)/$', views.DetailView.as_view(), name='detail'),
    url(r'^api/foos$', views.APIView, name="api")
]