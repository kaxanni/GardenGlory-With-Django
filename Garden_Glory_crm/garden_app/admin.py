from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Property)
admin.site.register(Services)
admin.site.register(Payment)
admin.site.register(Employee)
admin.site.register(Task)
admin.site.register(Equipment)
admin.site.register(TrainedEmployee)
admin.site.register(EquipmentUsage)
admin.site.register(EquipmentRepair)