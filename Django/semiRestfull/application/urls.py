from django.urls import path, include
from . import views

urlpatterns =[
    path('shows', views.dispShows),
    path('shows/new', views.dispAddShow),
    path('shows/<int:show_id>', views.dispOneShow),


    path('shows/addShow', views.addShow),
]