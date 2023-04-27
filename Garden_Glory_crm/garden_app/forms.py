from django.forms import ModelForm
from .models import Services, Customer, Property, Employee, Equipment

class ServiceForm(ModelForm):
    class Meta:
        model = Services
        fields = '__all__'
        
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class PropertyForm(ModelForm):
    class Meta:
        model = Property
        fields = '__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class EquipmentForm(ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'