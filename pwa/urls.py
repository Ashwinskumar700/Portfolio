from django.urls import path
from . import views

urlpatterns = [
    path('serviceworker.js', views.service_worker, name='service_worker'),
]
