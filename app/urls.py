from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="Home"),
    path('login/', views.login),
    path('send_email/', views.send_email, name='send_email'),
]
