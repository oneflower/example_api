from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [

    url(r'^category/(?P<pk>[0-9]+)/$', views.category_detail),
    url(r'^category/$', views.category_list),

    url(r'^entry/(?P<pk>[0-9]+)/$', views.entry_detail),
    url(r'^entry/$', views.entry_list),

]

urlpatterns = format_suffix_patterns(urlpatterns)
