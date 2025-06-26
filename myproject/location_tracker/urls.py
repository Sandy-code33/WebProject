from django.urls import path
from . import views

urlpatterns = [
    path('send-link/', views.send_tracking_link),
    path('track-location/<str:uuid>/', views.track_location, name='track-location'),
    path('save-location/', views.save_location),
]
