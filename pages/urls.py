from django.urls import path
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('about', views.about, name='about'),
    path('news', views.news, name='news'),
    path('links', views.links, name='links'),
    path('privacy', views.privacy, name='privacy'),
    path('terms', views.terms, name='terms'),
    path('pricing', views.pricing, name='pricing'),
    path('advertisers', views.advertisers, name='advertisers'),
    path('categories', views.categories, name='categories'),

]