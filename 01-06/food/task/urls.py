from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<id>/delete', views.deletemakan),
    path('<id>/edit', views.editmakan),
    path('minum/<id>/delete', views.deleteminum),
    path('<id>/edit', views.editminum),
]