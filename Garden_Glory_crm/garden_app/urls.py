from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('customer/<str:pk>/', views.customer, name="customer"),
    path('employee/', views.employee, name="employee"),
    path('employeeInfo/', views.employeeInfo, name="employeeInfo"),
    path('services/', views.services, name="services"),
    path('property/', views.property, name="property"),
    path('equipment/', views.equipment, name="equipment"),
    path('account/', views.account, name="account"),
    path('create_service/', views.createService, name="create_service"),
    path('update_service/<str:pk>/', views.updateService, name="update_service"),
    path('delete_service/<str:pk>/', views.deleteService, name="delete_service"),
    path('create_customer/', views.createCustomer, name="create_customer"),
    path('update_customer/<str:pk>/', views.updateCustomer, name="update_customer"),
    path('delete_customer/<str:pk>/', views.deleteCustomer, name="delete_customer"),
    path('create_property/', views.createProperty, name="create_property"),
    path('update_property/<str:pk>/', views.updateProperty, name="update_property"),
    # path('delete_property/<str:pk>/', views.deleteProperty, name="delete_property"),
    
]
