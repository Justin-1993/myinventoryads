from django.shortcuts import render
from django.http import HttpResponse

from categories.models import Categorie

# Create your views here.
def index(request):
    category = Categorie.objects.order_by('categories')

    context = {
        'categories': category
    }
    return render(request, 'pages/index.html', context)

def contact(request):
    return render(request, 'pages/contact.html')

def faq(request):
    return render(request, 'pages/faq.html')

def about(request):
    return render(request, 'pages/about.html')

def news(request):
    return render(request, 'pages/news.html')

def links(request):
    return render(request, 'pages/links.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

def terms(request):
    return render(request, 'pages/terms.html')

def pricing(request):
    return render(request, 'pages/membership.html')

def advertisers(request):
    return render(request, 'pages/advertisers.html')

def categories(request):
    category = Categorie.objects.order_by('categories')

    context = {
        'categories': category
    }
    return render(request, 'pages/categories.html', context)

