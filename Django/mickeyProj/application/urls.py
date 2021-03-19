from django.urls import path, include
from . import views

urlpatterns =[

    # Diplay routes
    path('', views.dispIndex),
    path('congrats', views.dispCongrats), # http://localhost:8000/congrats/
    path('form', views.dispMyForm),
    path('newTrip', views.dispNewTrip),

    # Action routes
    path('submit', views.getEmail),
    path('login', views.login),
    path('logout', views.logout),
    path('register', views.register),
    path('createNewTrip', views.createTrip),
    path('joinTrip/<int:tripID>', views.joinTrip),
    path('cancelTrip/<int:tripID>', views.cancelTrip),
]   