from django.conf.urls import url
from . import views
from . import formofurl
urlpatterns = [
    # url(r'^$',views.index, name = 'index'),
    url(r'^$',views.URL, name = 'add'),
    # url(r'^form/',views.add, name = 'form')
];