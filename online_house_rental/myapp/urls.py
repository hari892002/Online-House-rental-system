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
  path('propertyview/<int:id>/', views.propertyview, name='propertyview'),
  path('propertypage', views.propertypage, name='propertypage'),
  path('house', views.house, name='house'),
  path('updateprofile', views.updateprofile, name='updateprofile'),
  path('ownerupdate', views.ownerupdate, name='ownerupdate'),
  path('propertyadd', views.propertyadd, name='propertyadd'),
  path('ownerproperty', views.ownerproperty, name='ownerproperty'),
  path('logout', views.logout, name='logout'),
  path('manageproperty', views.manageproperty, name='manageproperty'),
  path('deactivate_user/<int:id>/',views. deactivate_user, name='deactivate_user'),
  path('activate_user/<int:id>/', views.activate_user, name='activate_user'),
  path('manage_users/<str:role>/', views.manage_users, name='manage_users'),
  path('view_profile/<int:user_id>/', views.view_profile, name='view_profile'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
