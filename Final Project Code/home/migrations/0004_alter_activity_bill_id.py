# Generated by Django 4.0.3 on 2022-03-22 02:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_bill_group_settlement_group_membership_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='bill_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='home.bill'),
        ),
    ]
