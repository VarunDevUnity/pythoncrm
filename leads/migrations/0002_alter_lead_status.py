# Generated by Django 5.2.1 on 2025-05-28 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='status',
            field=models.CharField(choices=[('new lead', 'New Lead'), ('in process', 'In Process'), ('quotation send', 'Quotation Send'), ('client onboard', 'Client Onboard'), ('cold', 'Cold'), ('closed', 'Closed'), ('follow up', 'Follow Up')], default='new lead', max_length=50),
        ),
    ]
