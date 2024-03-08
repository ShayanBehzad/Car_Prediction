from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='HomePage'),
    path('handle_choice/', views.handle_choice, name='handle_choice'),
    path("prediction/", views.prediction, name='prediction'),
]