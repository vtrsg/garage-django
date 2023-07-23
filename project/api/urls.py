from django.urls import path
from .views import (
    UserApi,
    BrandApi,
    ModelTypeApi,
    YearApi,
    CarApi,
)

urlpatterns = [
    path('usuario/', UserApi, name='user-list'),
    path('usuario/<int:id>/', UserApi, name='user-detail'),
    path('marca/', BrandApi, name='brand-list'),
    path('marca/<int:id>/', BrandApi, name='brand-detail'),
    path('modelo/', ModelTypeApi, name='model-list'),
    path('modelo/<int:id>/', ModelTypeApi, name='model-detail'),
    path('ano/', YearApi, name='year-list'),
    path('ano/<int:id>/', YearApi, name='year-detail'),
    path('carro/', CarApi, name='car-list'),
    path('carro/<int:id>/', CarApi, name='car-detail'),
]