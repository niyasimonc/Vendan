
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^place/order$', views.place_order, name='place_order'),
]
