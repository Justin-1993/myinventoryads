from django.urls import path

from . import views

urlpatterns = [
    path('', views.membership, name='membership'),
    path('standard/', views.standard, name='standard'),
    path('vip/', views.vip, name='vip'),
    path('cancel_vip/', views.cancel_vip, name='cancel_vip'),
    path('cancel_membership/', views.cancel_membership, name='cancel_membership')
]