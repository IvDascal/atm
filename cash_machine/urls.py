from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pin', views.pin, name='pin'),
    path('transaction', views.transaction, name='transaction'),
    path('balance', views.balance, name='balance'),
    path('withdraw', views.withdraw, name='withdraw'),
    path('error', views.error, name='error'),
]
