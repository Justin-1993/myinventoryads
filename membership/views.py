from django.shortcuts import redirect, render
from django.contrib.auth.models import User

from .models import Vip
from listings.models import Listing
# Create your views here.
def membership(request):
    return render(request, 'membership/membership.html')

def standard(request):
    if User.is_authenticated:
        if request.method == 'POST':
            username = request.user.id
            User.objects.filter(id=username).update(is_staff=True)
            print(username)
            return redirect('dashboard')
        else:
            return render(request, 'membership/standard.html')
    else:
        return redirect('register')

def vip(request):
        if User.is_authenticated:
            if request.method == 'POST':
                username = request.user.id
                User.objects.filter(id=username).update(is_staff=True)
                user_object = User.objects.get(id=username)
                Vip.objects.filter(user=user_object).update(is_vip=True)
                
                print(username)
                return redirect('dashboard')
            else:
                return render(request, 'membership/vip.html')
        else:
            return redirect('register')

def cancel_vip(request):
        if User.is_authenticated:
            if request.method == 'POST':
                username = request.user.id
                user_object = User.objects.get(id=username)
                Vip.objects.filter(user=user_object).update(is_vip=False)
                
                print(username)
                return redirect('index')
            else:
                return render(request, 'membership/cancel_vip.html')
        else:
            return redirect('register')

def cancel_membership(request):
        if User.is_authenticated:
            if request.method == 'POST':
                Listing.objects.filter(user=request.user.id).delete()
                username = request.user.id
                User.objects.filter(id=username).update(is_staff=False)
                user_object = User.objects.get(id=username)
                Vip.objects.filter(user=user_object).update(is_vip=False)
                
                return redirect('index')
            else:
                return render(request, 'membership/cancel_membership.html')
        else:
            return redirect('index')