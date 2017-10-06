from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^$', views.index, name = 'index'),
    url(r'post/$', views.post_list, name = 'post_list'),
    url(r'blog/$', views.blog, name = 'blog'),
    url(r'blog/details/(?P<id>\w{0,50})/$', views.details, name = 'details'),
    #url(r'^$', views.post_list, name='post_list'),

]
