# Generated by Django 3.2.16 on 2022-12-25 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingsys', '0004_alter_booking_start_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='party_size',
            field=models.CharField(choices=[('2', 'two_seater_window'), ('2', 'two_seater_corner'), ('4', 'four_seater_window'), ('4', 'four_seater_middle'), ('6', 'six_seater_corner'), ('6', 'six_seater_window'), ('6', 'six_seater_middle')], default='2', max_length=12, unique_for_date=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.CharField(choices=[('12:00', '12:00'), ('13:00', '13:00'), ('14:00', '14:00'), ('15:00', '15:00'), ('16:00', '16:00'), ('17:00', '17:00'), ('18:00', '18:00'), ('19:00', '19:00'), ('20:00', '20:00'), ('21:00', '21:00')], default='18:00', max_length=12),
        ),
    ]
