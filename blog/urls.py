from django.conf.urls import url
from . import views

"""/ ==> Qcceuil
   /post/1/ ==> detail des chaque poste
"""
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'home^$', views.home, name='home'),
    url(r'^apropos/$', views.apropos, name='apropos'),
    url(r'^electro/$', views.electronique, name='electronique'),
    url(r'^infor/$', views.informatique, name='informatique'),
    url(r'^hybride/$', views.hybride, name='hybride'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]