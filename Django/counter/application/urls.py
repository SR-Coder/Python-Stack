from django.urls import path
from . import views

urlpatterns = [
    # display route
    path('', views.index),

    # action route
    path('destroy_session', views.reset),
]