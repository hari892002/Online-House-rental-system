from django.shortcuts import render,redirect,get_object_or_404
from .models import User,Property,PropertyImage,Adminm
from django.contrib import messages
import logging
from django.utils.crypto import get_random_string
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.http import JsonResponse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.auth.tokens import default_token_generator

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def logout(request):
    request.session.flush()  # This clears the session data
    return redirect('login')


def index(request):
    return render(request, 'index.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email').strip().lower()
        password = request.POST.get('password')
        admin = Adminm.objects.filter(email=email).first()
        if admin:
            if admin.password == password:
                request.session['admin_email'] = admin.email
                return redirect('admin')
            else:
                return render(request, 'login.html', {'error': 'Incorrect password for admin'})
        user = User.objects.filter(email=email).first()
        if user:
            if user.password == password:
                request.session['user_id'] = user.id
                request.session['name'] = user.name
                request.session['role'] = user.role
                if user.role == 'owner':
                    return redirect('owner')
                elif user.role == 'user':
                    return redirect('userpage')
            else:
                return render(request, 'rename_login.html', {'error': 'Incorrect password'})
        return render(request, 'login.html', {'error': 'Email does not exist'})
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        phone = request.POST.get('contact')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirmPassword')
        role = request.POST.get('role')
        # Check if the email already exists
        if User.objects.filter(email=email).exists():
            return render(request, 'register.html', {
                'email_error': 'An account with this email already exists.',
                'name': name,
                'address': address,
                'contact': phone,
                'role': role,
            })
        # Check if the passwords match
        if password != confirm_password:
            return render(request, 'register.html', {
                'error': 'Passwords do not match.',
                'name': name,
                'address': address,
                'contact': phone,
                'email': email,
                'role': role,
            })

        # Create and save the new user
        user = User(name=name, address=address, email=email, phone=phone, password=password, role=role)
        user.save()

        # Send registration success email
        send_mail(
            'Registration Successful',
            f'Hello {name},\n\nThank you for registering!\n\nBest regards,\nYour Team',
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )

        return redirect('login')

    return render(request, 'register.html')



def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
def forgotpass(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user = User.objects.filter(email=email).first()
        if user:
            token = get_random_string(20)
            reset_link = request.build_absolute_uri(reverse('reset_password', args=[token]))
            try:
                send_mail(
                    'Password Reset Request',
                    f'Click the link below to reset your password:\n\n{reset_link}',
                    'your-email@example.com',  # Use the actual email configured in settings
                    [email],
                    fail_silently=False,
                )
                user.reset_token = token
                user.save()
                messages.success(request, 'Password reset link has been sent to your email.')
            except Exception as e:
                messages.error(request, f"Error sending email: {str(e)}")
        else:
            messages.error(request, 'No account found with that email.')
    return render(request, 'forgotpass.html')  # This should be inside the POST block


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def userpage(request):
    if request.session.get('user_id'):
        user_id = request.session.get('user_id')
        
        # Retrieve the logged-in user
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return redirect('login')  # Redirect to login if user not found
        properties = Property.objects.filter(is_verified=True)  # Only show verified properties

        # # Retrieve all properties (or filter them later based on the owner)
        # properties = Property.objects.all()

        # Get search parameters from the GET request
        location = request.GET.get('location', '')
        category = request.GET.get('category', '')
        price = request.GET.get('price', '')
        bhk = request.GET.get('bhk', '')

        # Filter properties based on the search criteria
        if location:
            properties = properties.filter(city__icontains=location) | properties.filter(state__icontains=location)
        
        
        if category:
            properties = properties.filter(property_type__iexact=category)
        
        if price:
            try:
                max_price = float(price)
                properties = properties.filter(price__lte=max_price)
            except ValueError:
                pass  # If price is not a valid number, skip this filter
        
        if bhk:
            try:
                bhk_value = int(bhk)
                properties = properties.filter(beds=bhk_value)
            except ValueError:
                pass  # If bhk is not a valid number, skip this filter

        # Pass the filtered properties to the template
        context = {
            'user': user,
            'properties': properties,
            'request': request  # Pass the request to the template for showing the form values
        }
        
        return render(request, 'userpage.html', context)
    else:
        return redirect('login')



@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def owner(request):
    if request.session.get('user_id'):
        user_id = request.session.get('user_id')  # Get user_id from session
        user = get_object_or_404(User, id=user_id)  # Fetch the user details

        owner_name = request.session.get('name')  # Get owner's name from session

        return render(request, 'owner.html', {
            'owner_name': owner_name,
            'user': user,  # Pass the user object to the template
        })
    else:
        return redirect('login')


def admin(request):
    return render(request, 'admin.html')
def reset_password(request, token):
    user = User.objects.filter(reset_token=token).first()
    if user:
        if request.method == 'POST':
            new_password = request.POST.get('new_password')
            confirm_password = request.POST.get('confirm_password')
            if new_password == confirm_password:
                user.password = new_password
                user.reset_token = None
                user.save()
                messages.success(request, 'Password reset successful. You can now log in.')
                return redirect('login')
            else:
                messages.error(request, 'Passwords do not match.')
        return render(request, 'reset_password.html', {'token': token})
    else:
        messages.error(request, 'Invalid or expired reset token.')
        return redirect('forgotpass')
def propertyview(request,id):
    # Use select_related to get the owner information in the same query
    property = get_object_or_404(Property,id=property_id)
    print(f"Owner Name: {property.owner.name}")  #  
    context = {
        'property': property,
    }
    return render(request, 'propertyview.html', context)

def propertypage(request):
    properties = Property.objects.all()  # Fetch all properties
    return render(request, 'propertypage.html', {'properties': properties})
def house(request):
    return render(request, 'house.html')

def updateprofile(request):
    if not request.session.get('user_id'):
        return redirect('login')
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_address = request.POST.get('address')
        new_phone = request.POST.get('phone')
        user.name = new_name
        user.address = new_address
        user.phone = new_phone
        user.save()
        return redirect('userpage')
    else:
        return render(request, 'updateprofile.html', {'user': user})
        
def ownerupdate(request):
    if not request.session.get('user_id'):
        return redirect('login')
    user_id = request.session.get('user_id')
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        new_name = request.POST.get('name')
        new_address = request.POST.get('address')
        new_phone = request.POST.get('phone')
        user.name = new_name
        user.address = new_address
        user.phone = new_phone
        user.save()
        return redirect('owner')
    else:
        return render(request, 'ownerupdate.html', {'user': user})

def propertyadd(request):
    if request.method == 'POST':
        property_name = request.POST.get('property_name')
        description = request.POST.get('description')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        price = request.POST.get('price')
        property_type = request.POST.get('property_type')
        listing_type = request.POST.get('listing_type')
        beds = request.POST.get('beds')
        baths = request.POST.get('baths')
        area = request.POST.get('area')
        owner_id = request.session.get('user_id')
        owner = User.objects.get(id=owner_id)
        if Property.objects.filter(property_name=property_name).exists():
            messages.error(request, "Property name already exists. Please choose another name.")
            return render(request, 'propertyadd.html')
        property_instance = Property.objects.create(
            property_name=property_name,description=description,address=address,city=city,state=state,price=price,
            property_type=property_type,listing_type=listing_type,beds=beds,baths=baths,area=area,owner=owner
        )
        property_photos = request.FILES.getlist('image')
        for photo in property_photos:
            PropertyImage.objects.create(property=property_instance, image=photo)
        messages.success(request, 'Property added successfully!')
        return redirect('owner')
    return render(request, 'propertyadd.html')
    
def updateproperty(request):
    property_instance = None
    search_property_name = request.GET.get('search_property_name')
    if search_property_name:
        property_instance = Property.objects.filter(property_name=search_property_name).first()
    if request.method == 'POST' and property_instance:
        property_instance.property_name = request.POST.get('property_name')
        property_instance.description = request.POST.get('description')
        property_instance.address = request.POST.get('address')
        property_instance.city = request.POST.get('city')
        property_instance.state = request.POST.get('state')
        property_instance.price = request.POST.get('price')
        property_instance.property_type = request.POST.get('property_type')
        property_instance.listing_type = request.POST.get('listing_type')
        property_instance.save()
        delete_image_id = request.POST.get('delete_image')
        if delete_image_id:
            image_to_delete = PropertyImage.objects.filter(id=delete_image_id, property=property_instance).first()
            if image_to_delete:
                image_to_delete.delete()
        new_images = request.FILES.getlist('new_images')
        for image in new_images:
            PropertyImage.objects.create(property=property_instance, image=image)
        return redirect(f"{reverse('owner')}?search_property_name={property_instance.property_name}")
    return render(request, 'updateproperty.html', {'property': property_instance})


def ownerproperty(request):
    properties = Property.objects.all()
    if request.method == 'POST':
        delete_image_id = request.POST.get('delete_image')
        delete_property_id = request.POST.get('delete_property')
        property_id = request.POST.get('property_id')
        if delete_image_id:
            property_instance = get_object_or_404(Property, id=property_id)
            image_to_delete = PropertyImage.objects.filter(id=delete_image_id, property=property_instance).first()
            if image_to_delete:
                image_to_delete.delete()
                return JsonResponse({'status': 'success'})
        property_instance = get_object_or_404(Property, id=property_id)
        property_instance.property_name = request.POST.get('property_name')
        property_instance.description = request.POST.get('description')
        property_instance.address = request.POST.get('address')
        property_instance.city = request.POST.get('city')
        property_instance.state = request.POST.get('state')
        property_instance.price = request.POST.get('price')
        property_instance.property_type = request.POST.get('property_type')
        property_instance.listing_type = request.POST.get('listing_type')
        property_instance.save()
        new_images = request.FILES.getlist('new_images')
        for image in new_images:
            PropertyImage.objects.create(property=property_instance, image=image)
        return redirect('ownerproperty')
    return render(request, 'ownerproperty.html', {'properties': properties})

def manageproperty(request):
    properties = Property.objects.all()  # Fetch all properties
    return render(request, 'manageproperty.html', {'properties': properties})

def manage_users(request, role):
    users = User.objects.filter(role=role)
    context = {'users': users, 'role': role}
    return render(request, 'manage_users.html', context)
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('manage_users', user.role)

def view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'view_profile.html', {'user': user})

def view_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    return render(request, 'view_profile.html', {'user': user})

def deactivate_user(request, id):
    user = get_object_or_404(User, id=id)
    user.status = False  # Set the status to inactive
    user.save()

    # Send an email notification
    send_mail(
        'Account Deactivation',
        f'Hello {user.name},\n\nYour account has been deactivated. If you have any questions, please contact support.',
        'your_email@example.com',  # Replace with your email or from_email
        [user.email],
        fail_silently=False,
    )

    messages.success(request, 'User has been deactivated and notified via email.')
    
    # Redirect to manage_users with the role parameter
    return redirect('manage_users', role=user.role)  # Adjust user.role based on how you retrieve it

def activate_user(request, id):
    user = get_object_or_404(User, id=id)
    user.status = True  # Set the status to active
    user.save()

    # Send an email notification
    send_mail(
        'Account Activation',
        f'Hello {user.name},\n\nYour account has been activated. You can now log in and use our services.',
        'your_email@example.com',  # Replace with your email or from_email
        [user.email],
        fail_silently=False,
    )

    messages.success(request, 'User has been activated and notified via email.')

    # Redirect to manage_users with the role parameter
    return redirect('manage_users', role=user.role)  # Adjust user.role based on how you retrieve it

def request(request):
    properties = Property.objects.all()  # Retrieve all properties
    return render(request, 'request.html', {'properties': properties})

def verify_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    property.is_verified = True  # Set is_verified to 1
    property.save()

    # Send verification email
    send_mail(
        'Property Verified',
        f'Congratulations! Your property "{property.property_name}" has been verified by our team.',
        'your_email@example.com',  # Replace with your email
        [property.owner.email],  # Owner's email
        fail_silently=False,
    )

    messages.success(request, f'Property "{property.property_name}" has been verified.')
    return redirect('request')  # Redirect back to the request page


def reject_property(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    property.is_verified = False  # Set is_verified to 0
    property.save()

    # Send rejection email
    send_mail(
        'Property Rejected',
        f'We regret to inform you that your property "{property.property_name}" has been rejected by our team.',
        'your_email@example.com',  # Replace with your email
        [property.owner.email],  # Owner's email
        fail_silently=False,
    )

    messages.success(request, f'Property "{property.property_name}" has been rejected.')
    return redirect('request')


def add_to_wishlist(request, property_id):
    property = get_object_or_404(Property, id=property_id, status=1, is_verified=1)  # Only allow active and verified properties

    # Get the wishlist from session or initialize an empty list
    wishlist = request.session.get('wishlist', [])

    # Add the property to wishlist if not already added
    if property_id not in wishlist:
        wishlist.append(property_id)
        request.session['wishlist'] = wishlist  # Save the wishlist back to session

    return redirect('wishlist')  # Redirect to the 

def remove_from_wishlist(request, property_id):
    wishlist = request.session.get('wishlist', [])

    if property_id in wishlist:
        wishlist.remove(property_id)
        request.session['wishlist'] = wishlist  # Save the updated wishlist back to session

    return redirect('wishlist')

def wishlist(request):
    # Get the wishlist from session
    wishlist = request.session.get('wishlist', [])

    # Fetch the properties from the wishlist
    properties = Property.objects.filter(id__in=wishlist, status=1, is_verified=1)  # Only show active and verified properties

    return render(request, 'wishlist.html', {'properties': properties})

def bookproperty(request):
    return render(request, 'bookproperty.html')
def bookconf(request):
    return render(request, 'bookconf.html')

def contactowner(request, property_id):
    # Retrieve the property and pass it to the template
    property = get_object_or_404(Property, id=property_id)
    context = {
        'property': property,  # Pass the property object to access its id in the template
    }
    return render(request, 'contactowner.html', context)


def owner_details(request, property_id):
    property_obj = get_object_or_404(Property, id=property_id)
    owner = property_obj.owner

    context = {
        'property_id': property_id,
        'owner_name': owner.name,
        'owner_phone': owner.phone,
        'is_phone_verified': owner.is_verified,  # Assuming 'is_verified' is a field for phone verification
    }

    return render(request, 'owner_details.html', context)