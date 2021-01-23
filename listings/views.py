from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import Q

from categories.models import Categorie
from .models import Listing
from membership.models import Vip

def index(request):
    all_listings = Listing.objects.all()
    context = {
        'listings': all_listings,
    }
    return render(request, 'listings/listings.html',context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    
    queryset_list = Listing.objects.all()

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter( Q(description__icontains=keywords) | Q(title__icontains=keywords) | Q(part_number__icontains=keywords) | Q(category__categories__icontains=keywords) | Q(state__icontains=keywords) | Q(city__icontains=keywords) | Q(website_url__icontains=keywords))

    if 'category' in request.GET:
        category = request.GET['category']
        if category:
            queryset_list = queryset_list.filter(category__categories__icontains=category)
    
    if 'zip' in request.GET:
        zip = request.GET['zip']
        if zip:
            queryset_list = queryset_list.filter(zipcode__iexact=zip)

    context = {
        'listings': queryset_list
    }
    
    return render(request, 'listings/search.html', context) 