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
  path('deactivate_user/<int:id>/', views.deactivate_user, name='deactivate_user'),
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
  path('rental-agreement/<int:property_id>/', views.rental_agreement, name='rental_agreement'),
  path('adminproview', views.adminproview, name='adminproview'),
  path('propertywelcom', views.propertywelcom, name='propertywelcom'),
  path('terms/<int:property_id>/', views.termsandconditions, name='termsandconditions'),
  path('ownerview/', views.ownerview, name='ownerview'),  
  path('accept-decline-agreement/<int:agreement_id>/', views.accept_decline_agreement, name='accept_decline_agreement'),
  path('rented-properties/', views.rented_properties_view, name='rented_properties'),
  path('buy-property/<int:property_id>/', views.buy_property, name='buy_property'),
  path('vra/', views.userviewrental, name='userviewrental'),
  path('verify-otp/', views.verify_otp, name='verify_otp'),
  path('enter-email/',views.enter_email, name='enter_email'),
  path('notification', views.notification, name='notification'),
  path('notification/clear/<int:message_id>/', views.clear_message, name='clear_message'),
  path('property/<int:property_id>/conversation/', views.conversation, name='conversation'),
  path('property/<int:property_id>/send_message/', views.send_message, name='send_message'),
  path('certificate/<int:agreement_id>/', views.certificate, name='certificate'),
  path('owner/conversation/<int:property_id>/', views.owner_conversation, name='owner_conversation'),
  path('clear_messages/<int:sender_id>/<int:property_id>/', views.clear_messages, name='clear_messages'),
  path('owner/conversation/viewuser/<int:property_id>/', views.owner_conversation_viewuser, name='owner_conversation_view'),
  path('notification_owner', views.notification_owner, name='notification_owner'),
  path('clear_message/<int:sender_id>/<int:property_id>/', views.clear_message, name='clear_message'),
  path('owner/conversation/<int:property_id>/clear/', views.clear_owner_messages, name='clear_owner_messages'),
  path('buyer/', views.buyer, name='buyer'),
  path('biling_details/<int:payment_id>/', views.biling_details, name='biling_details'),
  path('thank', views.thank, name='thank'),
  path('property/<int:property_id>/feedback/',views.feedback_page, name='feedback_page'),
  path('owner/view_feedback/', views.owner_feedback_view, name='owner_feedback_view'),
  path('create-order/<int:payment_id>/', views.create_order, name='create-order'),
  path('payment-success/', views.payment_success, name='payment-success'),
  path('adminfeedback/', views.admin_feedback, name='admin_feedback'),
  path('proceedtopayment/', views.proceedtopayment, name='proceedtopayment'),
  path('proceedtopaymentview/', views.proceedtopaymentview, name='proceedtopaymentview'),
  path('create-ordersss/<int:payment_id>/', views.create_ordersss, name='create_ordersss'),
  path('token-advance_list/', views.token_advance_list, name='token_advance_list'),
  # path('buy_details', views.buy_details, name='buy_details'),
  # path('create-ordersss/<int:property_id>/', views.create_ordersss, name='create_ordersss'),
  path('chat/', views.chat_with_bot, name='chat_with_bot'),
  path('chat-interface/', views.chatbot_page, name='chatbot_page'),
  path('owner/dashboard/', views.owner_dashboard, name='owner_dashboard'),
  path('owner/property-data/', views.owner_property_data, name='owner_property_data'),
  path('service-providers/', views.service_providers, name='service_providers'),
  path('maintanence', views.maintanence, name='maintanence'),
  path('maintenance/<int:property_id>/', views.maintenance_request, name='maintenance_request'),
  path('owner/maintenance/', views.owner_maintenance_requests, name='owner_maintenance'),
  path('maintenance/update/<int:request_id>/', views.update_maintenance_status, name='update_maintenance_status'),
  path('maintenance/notes/<int:request_id>/', views.update_maintenance_notes, name='update_maintenance_notes'),
  path('household-items/', views.household_items, name='household_items'),
  path('rental_compliance/', views.rental_compliance, name='rental_compliance'),
  path('predict/', views.predict_price, name='predict_price'),
  path('adminhousehold-items/', views.admin_household_items, name='admin_household_items'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
