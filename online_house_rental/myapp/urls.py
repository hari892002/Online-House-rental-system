from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
  path('', views.index, name='index'),
  path('login', views.login, name='login'),
  path('register', views.register, name='register'),
  path('about', views.about, name='about'),
  path('contact', views.contact, name='contact'),
  path('forgotpass', views.forgotpass, name='forgotpass'),
  path('userpage', views.userpage, name='userpage'),
  path('owner', views.owner, name='owner'),
  path('admin', views.admin, name='admin'),
  path('reset_password/<str:token>/', views.reset_password, name='reset_password'),
  path('propertyview/<int:property_id>/', views.propertyview, name='propertyview'),
  path('propertypage', views.propertypage, name='propertypage'),
  path('updateprofile', views.updateprofile, name='updateprofile'),
  path('ownerupdate', views.ownerupdate, name='ownerupdate'),
  path('propertyadd', views.propertyadd, name='propertyadd'),
  path('logout', views.logout, name='logout'),
  path('manageproperty', views.manageproperty, name='manageproperty'),
  path('deactivate_user/<int:id>/',views. deactivate_user, name='deactivate_user'),
  path('activate_user/<int:id>/', views.activate_user, name='activate_user'),
  path('manage_users/<str:role>/', views.manage_users, name='manage_users'),
  path('view_profile/<int:user_id>/', views.view_profile, name='view_profile'),
  path('request', views.request, name='request'),
  path('verify_property/<int:property_id>/', views.verify_property, name='verify_property'),
  path('reject_property/<int:property_id>/', views.reject_property, name='reject_property'),
  path('bookproperty', views.bookproperty, name='bookproperty'),
  path('bookconf', views.bookconf, name='bookconf'),
  path('contactowner/<int:property_id>/', views.contactowner, name='contactowner'), 
  path('ownerproperty', views.ownerproperty, name='ownerproperty'),
  path('owner_details/<int:property_id>/', views.owner_details, name='owner_details'),
  path('wishlist/', views.wishlist, name='wishlist'),
  path('chat/user/<int:owner_id>/', views.user_chat_view, name='user_chat'),
  path('chat/owner/<int:user_id>/', views.owner_chat_view, name='owner_chat'),
  path('rental-agreement/<int:property_id>/', views.rental_agreement, name='rental_agreement'),
  path('adminproview', views.adminproview, name='adminproview'),
  path('propertywelcom', views.propertywelcom, name='propertywelcom'),
  path('terms/<int:property_id>/', views.termsandconditions, name='termsandconditions'),
  


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
