from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^page=(?P<page>\d+)$', views.index, name='index'),
    url(r'^(?P<pk>\d+)/$',views.Post.as_view(),name='blog')

]
