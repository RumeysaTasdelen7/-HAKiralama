from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('<int:imageId>/add/', views.IhaAddView.as_view(), name='iha-add'),
    path('all/', views.IhaListView.as_view(), name='iha-list'),
    path('<int:pk>/', views.IhaDetail.as_view(), name='iha-detail'),
]

