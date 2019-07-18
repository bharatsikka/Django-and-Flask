from django.conf.urls import url
from . import views
from . import forms
urlpatterns = [
    # url(r'^$',views.index, name = 'index'),
    url(r'^$',views.add, name = 'add'),
    # url(r'^form/',views.add, name = 'form')
];