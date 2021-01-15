from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('add_listing', views.add_listing, name='add_listing'),
    path('delete_listing/<int:listing_id>', views.delete_listing, name='delete_listing')
 
]