from django.db import models
from django.core.exceptions import ValidationError
from random import randint
import random
import uuid

# Create your models here.

class Customer(models.Model):

    CUSTOMER_TYPE_CHOICES = [
        ('INDIVIDUAL', 'Individual'),
        ('CORPORATION', 'Corporation'),
    ]
    customer_id = models.IntegerField(primary_key=True, unique=True, default=random.randint(1000000000, 9999999999))
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    customer_type = models.CharField(max_length=110, null=True, choices=CUSTOMER_TYPE_CHOICES)

    def clean(self):
        if not self.email and not self.contact_number:
            raise ValidationError("At least one of email or contact number must be provided.")
    
    def __str__(self):
        return f"{self.name}"
    
class Property(models.Model):
    property_id = models.IntegerField(primary_key=True, unique=True, default=random.randint(1000000000, 9999999999))
    property_name= models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)
    state = models.CharField(max_length=50, blank =True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.property_name}"
    
class Services(models.Model):
    MAINTENANCE= 'Maintenance'
    ONE_TIME= 'One-time'
    ON_GOING= 'On going'

    REQUEST_TYPE_CHOICES = [
        (MAINTENANCE, 'MAINTENANCE'),
        (ONE_TIME, 'ONE-TIME'),
        (ON_GOING, 'ON GOING'),
    ]

    service_id = models.IntegerField(primary_key=True, unique=True, default=random.randint(1000000000, 9999999999))
    service_request = models.CharField(max_length=255)
    request_type = models.CharField(max_length=11, null=True, choices=REQUEST_TYPE_CHOICES, default='MAINTENANCE')
    request_date = models.DateField()
    customer = models.ManyToManyField(Customer, related_name="services")
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='services')
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
         return f"Service ID: {self.service_id}"
    
class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Credit Card'),
        ('debit_card', 'Debit Card'),
        ('paypal', 'PayPal'),
        ('bank_transfer', 'Bank Transfer'),
    ]
    payment_id = models.IntegerField(primary_key=True, unique=True, default=random.randint(1000000000, 9999999999))
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, max_length=20)
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)

        
    def __str__(self):
        return f"Payment {self.payment_id} - {self.payment_method}"

    class Meta:
        verbose_name_plural = "Payments"

class Employee(models.Model):
    EMPLOYEE_TYPES = [
        ('full_time', 'Full-time'),
        ('part_time', 'Part-time'),
        ('contractor', 'Contractor'),
        ('administrative_assistant', 'Administrative Assistant'),
        ('management', 'Management'),
        ('administrator', 'Administrator'),
    ]
    EMPLOYEE_STATUSES = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
    ]
    EXPERIENCE_LEVELS = [
        ('entry', 'Entry-level'),
        ('intermediate', 'Intermediate'),
        ('senior', 'Senior'),
    ]
    employee_id = models.IntegerField(primary_key=True, unique=True, default=random.randint(1000000000, 9999999999))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=20)
    experience_level = models.CharField(max_length=20, null=True, choices=EXPERIENCE_LEVELS)
    total_hours_worked = models.PositiveIntegerField(default=0)
    employee_type = models.CharField(max_length=30, null=True, choices=EMPLOYEE_TYPES)
    employee_status = models.CharField(max_length=20, null=True, choices=EMPLOYEE_STATUSES, default='active')
    services = models.ManyToManyField(Services, related_name="employee")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
class Task(models.Model):
    task_id = models.IntegerField(primary_key=True, unique=True, default=random.randint(1000000000, 9999999999))
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    service = models.ForeignKey(Services, on_delete=models.CASCADE)
    task_name = models.CharField(max_length=100)
    hrs_work = models.IntegerField()
    date_conducted = models.DateField()

    def __str__(self):
        return f"Task Name: {self.task_name}"
    
class Equipment(models.Model):
    equipment_id =models.IntegerField(primary_key=True, unique=True, default=random.randint(1000000000, 9999999999))
    equipment_name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    def __str__(self):
        return self.equipment_name
    
class TrainedEmployee(models.Model):
    trained_employee_id = models.IntegerField(primary_key=True, unique=True, default=random.randint(1000000000, 9999999999))
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.trained_employee_id} - {self.employee.first_name} {self.employee.last_name} - {self.equipment.equipment_name}"

    class Meta:
        verbose_name_plural = "Trained Employees"

class EquipmentUsage(models.Model):
    equipment_usage_id = models.IntegerField(primary_key=True, unique=True, default=random.randint(1000000000, 9999999999))
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    task = models.ForeignKey('Task', on_delete=models.CASCADE)
    usage_description = models.TextField()

    def __str__(self):
        return f"Equipment Usage {self.equipment_usage_id}"
    
class EquipmentRepair(models.Model):
    equipment_repair_id = models.IntegerField(primary_key=True, unique=True, default=random.randint(1000000000, 9999999999))
    equipment_id = models.ForeignKey('Equipment', on_delete=models.CASCADE)
    repair_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    remarks = models.TextField()

    def __str__(self):
        return f"{self.equipment_repair_id} - {self.equipment_id} - {self.repair_date}"

class Account(models.Model):
    account_id = models.AutoField(primary_key=True)
    employee_id = models.ForeignKey('Employee', on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    role_type = models.CharField(max_length=100)

    def __str__(self):
        return self.username


