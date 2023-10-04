# Generated by Django 4.1.7 on 2023-10-04 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carbrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carbrand', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CarData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carIDE', models.PositiveIntegerField(choices=[(100000, 1), (200000, 2), (300000, 3), (400000, 4), (500000, 5), (600000, 6), (700000, 7), (800000, 8), (900000, 9), (1000000, 10)])),
                ('caryear', models.IntegerField(choices=[('', ''), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022), (2023, 2023)], default=2023)),
                ('transmission', models.CharField(choices=[('Manual', 'Manual'), ('Automatic', 'Automatic')], default='', max_length=9)),
                ('kilometers', models.IntegerField(choices=[('', ''), (10000, 10000), (20000, 20000), (30000, 30000), (40000, 40000), (50000, 50000), (60000, 60000), (70000, 70000), (80000, 80000), (90000, 90000), (100000, 100000), (110000, 110000), (120000, 120000), (130000, 130000), (140000, 140000), (150000, 150000)], default=0)),
                ('ownership', models.CharField(choices=[('', ''), ('1st', '1st'), ('2nd', '2nd'), ('3rd', '3rd'), ('dealer', 'dealer')], default='', max_length=6)),
                ('fuletype', models.CharField(choices=[('CNG', 'CNG'), ('Petrol', 'Petrol'), ('Diesel', 'Diesel')], default='', max_length=6)),
                ('price', models.PositiveIntegerField(default=0)),
                ('city', models.CharField(default='', max_length=50)),
                ('carbrand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cardata.carbrand')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Carmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carmodel', models.CharField(default='', max_length=100)),
                ('mileage', models.CharField(default='', max_length=50)),
                ('doors', models.IntegerField()),
                ('power', models.CharField(max_length=50)),
                ('boot_space', models.CharField(max_length=50)),
                ('seating_capacity', models.IntegerField(default=5)),
                ('max_torque', models.CharField(max_length=50)),
                ('carbrand', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Cardata.carbrand')),
            ],
        ),
        migrations.CreateModel(
            name='CarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_images/')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cardata.cardata')),
            ],
        ),
        migrations.AddField(
            model_name='cardata',
            name='carmodel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cardata.carmodel'),
        ),
    ]