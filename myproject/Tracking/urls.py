from django.urls import path
from . import views, api

urlpatterns = [
    path('', views.track_order_page, name='track_order'),
    path('api/track/<str:order_id>/', api.track_order_api, name='track_order_api'),
]
