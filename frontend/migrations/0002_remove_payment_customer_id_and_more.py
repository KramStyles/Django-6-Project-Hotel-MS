# Generated by Django 4.0.3 on 2022-04-09 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_type_id',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='receptionist',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='customer_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='payment_type_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='room_id',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='staff_id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_status_id',
        ),
        migrations.RemoveField(
            model_name='room',
            name='room_type_id',
        ),
        migrations.DeleteModel(
            name='Booking',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Payment_type',
        ),
        migrations.DeleteModel(
            name='Receptionist',
        ),
        migrations.DeleteModel(
            name='Reservation',
        ),
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.DeleteModel(
            name='Room_status',
        ),
        migrations.DeleteModel(
            name='Room_type',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
