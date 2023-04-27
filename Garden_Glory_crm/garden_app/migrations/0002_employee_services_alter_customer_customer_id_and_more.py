# Generated by Django 4.1.7 on 2023-04-03 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('garden_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='services',
            field=models.ManyToManyField(related_name='employee', to='garden_app.services'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='customer_id',
            field=models.IntegerField(default=3938458819, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_id',
            field=models.IntegerField(default=7127736747, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='equipment_id',
            field=models.IntegerField(default=2664672519, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='equipmentrepair',
            name='equipment_repair_id',
            field=models.IntegerField(default=5310247690, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='equipmentusage',
            name='equipment_usage_id',
            field=models.IntegerField(default=7734786147, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_id',
            field=models.IntegerField(default=8698467914, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_id',
            field=models.IntegerField(default=4466960267, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='services',
            name='service_id',
            field=models.IntegerField(default=3703207945, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_id',
            field=models.IntegerField(default=2882406557, primary_key=True, serialize=False, unique=True),
        ),
        migrations.AlterField(
            model_name='trainedemployee',
            name='trained_employee_id',
            field=models.IntegerField(default=3745394410, primary_key=True, serialize=False, unique=True),
        ),
    ]