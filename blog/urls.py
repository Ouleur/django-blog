from django.conf.urls import url
from . import views

"""/ ==> Qcceuil
   /post/1/ ==> detail des chaque poste
"""
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]