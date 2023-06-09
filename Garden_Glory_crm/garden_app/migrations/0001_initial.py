# Generated by Django 4.1.7 on 2023-04-03 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(default=7887823271, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('contact_number', models.CharField(blank=True, max_length=20, null=True)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('customer_type', models.CharField(choices=[('INDIVIDUAL', 'Individual'), ('CORPORATION', 'Corporation')], max_length=110, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employee_id', models.IntegerField(default=7736334681, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('experience_level', models.CharField(choices=[('entry', 'Entry-level'), ('intermediate', 'Intermediate'), ('senior', 'Senior')], max_length=20, null=True)),
                ('total_hours_worked', models.PositiveIntegerField(default=0)),
                ('employee_type', models.CharField(choices=[('full_time', 'Full-time'), ('part_time', 'Part-time'), ('contractor', 'Contractor'), ('administrative_assistant', 'Administrative Assistant'), ('management', 'Management'), ('administrator', 'Administrator')], max_length=30, null=True)),
                ('employee_status', models.CharField(choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('equipment_id', models.IntegerField(default=2029743947, primary_key=True, serialize=False, unique=True)),
                ('equipment_name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('property_id', models.IntegerField(default=8362166874, primary_key=True, serialize=False, unique=True)),
                ('property_name', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zip_code', models.CharField(max_length=10)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('service_id', models.IntegerField(default=2009214597, primary_key=True, serialize=False, unique=True)),
                ('service_request', models.CharField(max_length=255)),
                ('request_type', models.CharField(choices=[('Maintenance', 'MAINTENANCE'), ('One-time', 'ONE-TIME'), ('On going', 'ON GOING')], default='MAINTENANCE', max_length=11, null=True)),
                ('request_date', models.DateField()),
                ('customer', models.ManyToManyField(related_name='services', to='garden_app.customer')),
                ('equipment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='garden_app.equipment')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='services', to='garden_app.property')),
            ],
        ),
        migrations.CreateModel(
            name='TrainedEmployee',
            fields=[
                ('trained_employee_id', models.IntegerField(default=1017560705, primary_key=True, serialize=False, unique=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_app.employee')),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_app.equipment')),
            ],
            options={
                'verbose_name_plural': 'Trained Employees',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.IntegerField(default=7840794425, primary_key=True, serialize=False, unique=True)),
                ('task_name', models.CharField(max_length=100)),
                ('hrs_work', models.IntegerField()),
                ('date_conducted', models.DateField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_app.employee')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_app.services')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('payment_id', models.IntegerField(default=2685314410, primary_key=True, serialize=False, unique=True)),
                ('payment_method', models.CharField(choices=[('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('paypal', 'PayPal'), ('bank_transfer', 'Bank Transfer')], max_length=20)),
                ('payment_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('services', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_app.services')),
            ],
            options={
                'verbose_name_plural': 'Payments',
            },
        ),
        migrations.CreateModel(
            name='EquipmentUsage',
            fields=[
                ('equipment_usage_id', models.IntegerField(default=8085312549, primary_key=True, serialize=False, unique=True)),
                ('usage_description', models.TextField()),
                ('equipment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_app.equipment')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_app.task')),
            ],
        ),
        migrations.CreateModel(
            name='EquipmentRepair',
            fields=[
                ('equipment_repair_id', models.IntegerField(default=8499633669, primary_key=True, serialize=False, unique=True)),
                ('repair_date', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=10)),
                ('remarks', models.TextField()),
                ('equipment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_app.equipment')),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('account_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('role_type', models.CharField(max_length=100)),
                ('employee_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garden_app.employee')),
            ],
        ),
    ]
