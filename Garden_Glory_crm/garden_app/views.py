from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from .forms import *
# Create your views here.

def home(reqeust):
    customers= Customer.objects.all()
    total_customer=customers.count()
    indiv_cus=customers.filter(customer_type='INDIVIDUAL').count()
    corp_cus=customers.filter(customer_type='CORPORATION').count()
    context= {'customers': customers, 'total_customer': total_customer,
              'indiv_cus': indiv_cus, 'corp_cus':corp_cus}
    return render(reqeust, 'garden_app/dashboard.html', context)

def customer(reqeust, pk):
    customer = Customer.objects.get(customer_id=pk)
    services = customer.services.all()
    services_count= services.count()
    context ={'customer': customer, 'services': services, 'services_count': services_count}
    return render(reqeust, 'garden_app/customer.html', context)

def employee(reqeust):
    employees= Employee.objects.all()
    context= {'employees': employees}
    return render(reqeust, 'garden_app/employee.html',context)

def employeeInfo(reqeust, pk):
    employeeInfo = Employee.objects.get(employee_id=pk)
    services = employeeInfo.services.all()
    context= {'employeeInfo': employeeInfo, 'services': services}
    return render(reqeust, 'garden_app/employeeInfo.html',context)

def services(reqeust):  
    services= Services.objects.all()
    context = {'services': services}
    return render(reqeust, 'garden_app/services.html', context)

def property(reqeust):
    properties=Property.objects.all()
    context= {'properties': properties}
    return render(reqeust, 'garden_app/property.html', context)

def equipment(reqeust):
    equipments= Equipment.objects.all()
    context = {'equipments': equipments}
    return render(reqeust, 'garden_app/equipment.html', context)

def account(reqeust):
    accounts=Account.objects.all()
    context= {'accounts': accounts}
    return render(reqeust, 'garden_app/account.html', context)

def createService(request):
    form = ServiceForm()
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context={'form':form}
    return render(request, 'garden_app/service_form.html', context)

def updateService(request, pk):
    service = Services.objects.get(service_id=pk)
    form = ServiceForm(instance=service)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=service)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'garden_app/service_form.html', context)

def deleteService(request, pk):
    service = Services.objects.get(service_id=pk)
    if request.method == "POST":
        service.delete()
        return redirect('/')
    context = {'item': service}
    return render(request, 'garden_app/delete.html', context)

def createCustomer(request):
    form = CustomerForm()
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context={'form':form}
    return render(request, 'garden_app/customer_form.html', context)

def updateCustomer(request, pk):
    customer = Customer.objects.get(customer_id=pk)
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'garden_app/customer_form.html', context)

def deleteCustomer(request, pk):
    customer = Customer.objects.get(customer_id=pk)
    if request.method == "POST":
        customer.delete()
        return redirect('/')
    context = {'item': customer}
    return render(request, 'garden_app/delete_customer.html', context)

def createProperty(request):
    form = PropertyForm()
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context={'form':form}
    return render(request, 'garden_app/property_form.html', context)

def updateProperty(request, pk):
    property = Property.objects.get(property_id=pk)
    form = PropertyForm(instance=property)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'garden_app/property_form.html', context)