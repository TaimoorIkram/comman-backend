# Generated by Django 4.2 on 2023-11-29 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0002_employeetype_paymenttype'),
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='employee_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='hrm.member'),
        ),
    ]
