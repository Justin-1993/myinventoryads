from django.shortcuts import redirect, render
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render


from listings.models import Listing
from categories.models import Categorie

# Create your views here.
def register(request):
    if request.method == 'POST':
        # register user
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        
        if password == password2:
            #check username
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username is already taken")
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, "Email is already taken")
                    return redirect('register')
                else:
                    # Create User
                    user = User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                    # Login after creation
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in')
                    return redirect('index')
        else:
            # Check passwords
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')





def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid Login')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('index')

def dashboard(request):
    my_listings = Listing.objects.filter(user=request.user)
    context = {
        'my_listings': my_listings
    }
    
    if request.user.is_authenticated and request.user.is_staff:
        return render(request, 'accounts/dashboard.html', context)
    else:
        return redirect('index')

    

def add_listing(request):
    category = Categorie.objects.order_by('categories')
    context = {
        'categories': category
    }
    if request.user.is_authenticated and request.user.is_staff:
        if request.method == 'POST':
            try:
                if request.POST.get('title') and request.POST.get('category') and request.POST.get('part_number') and request.POST.get('contact_email') and request.POST.get('website_url') and request.POST.get('contact_number') and request.POST.get('address') and request.POST.get('city') and request.POST.get('state') and request.POST.get('zipcode') and request.POST.get('description') and request.POST.get('price') and request.FILES.get('photo_main'):
                    current_user = request.user
                    user_id = current_user.id
                    user_object = User.objects.get(id=user_id)
                    cat_name = request.POST.get('category')
                    cat_id = Categorie.objects.get(categories=cat_name)
                    post = Listing()
                    post.user = user_object
                    post.category = cat_id
                    post.title = request.POST.get('title')
                    post.part_number = request.POST.get('part_number')
                    post.contact_email = request.POST.get('contact_email')
                    post.website_url = request.POST.get('website_url')
                    post.phone = request.POST.get('contact_number')
                    post.address = request.POST.get('address')
                    post.city = request.POST.get('city')
                    post.state = request.POST.get('state')
                    post.zipcode = request.POST.get('zipcode')
                    post.price = request.POST.get('price')
                    post.description = request.POST.get('description')
                    post.photo_main = request.FILES.get('photo_main')
                    post.save()
                    messages.success(request, 'Listing has been added!')
                    return render(request, 'accounts/add_listing.html', context)
                else:
                    messages.error(request, 'Not everything was filled out')
                    return render(request, 'accounts/add_listing.html', context)
            except:
                messages.error(request, 'Something went wrong...')
                return render(request, 'accounts/add_listing.html', context)
        else:
            return render(request, 'accounts/add_listing.html', context)
    else:
        return redirect('index')

def delete_listing(request, listing_id):
    listings = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listings
    }
    if User.is_authenticated and User.is_staff and request.user.id == listings.user.id:
        if request.method == 'POST':
            print(listings.id)
            instance = Listing.objects.get(id=listings.id)
            instance.delete()
            return redirect('dashboard')
        else:
            return render(request, 'accounts/delete_listing.html', context)
    else:
        return redirect('dashboard')