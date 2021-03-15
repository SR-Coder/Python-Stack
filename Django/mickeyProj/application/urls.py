from django.urls import path, include
from . import views

urlpatterns =[

    # Diplay routes
    path('', views.dispIndex),
    path('congrats/<str:name>', views.dispCongrats), # http://localhost:8000/congrats/
    path('form', views.dispMyForm),

    # Action routes
    path('submit', views.getEmail),
]   