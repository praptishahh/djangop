# Generated by Django 3.2.7 on 2021-12-12 05:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=150)),
                ('pincode', models.CharField(max_length=6)),
            ],
            options={
                'db_table': 'bloodbank_area',
            },
        ),
        migrations.CreateModel(
            name='Blood_grp',
            fields=[
                ('bloodgrp_id', models.AutoField(primary_key=True, serialize=False)),
                ('bloodgrp_type', models.CharField(max_length=5)),
            ],
            options={
                'db_table': 'bloodbank_bloods_grp',
            },
        ),
        migrations.CreateModel(
            name='Bloodbank',
            fields=[
                ('b_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_name', models.CharField(max_length=50)),
                ('b_address', models.CharField(max_length=300)),
                ('b_email', models.EmailField(max_length=254, unique=True)),
                ('b_pwd', models.CharField(max_length=15)),
                ('b_contact', models.CharField(max_length=15)),
                ('b_timing', models.DateTimeField()),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.area')),
            ],
            options={
                'db_table': 'bloodbank_bloodbank',
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('e_name', models.CharField(max_length=100)),
                ('e_date', models.DateField()),
                ('e_des', models.CharField(max_length=500)),
                ('e_img', models.ImageField(upload_to='')),
                ('e_location', models.CharField(max_length=200)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.area')),
                ('b_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.bloodbank')),
            ],
            options={
                'db_table': 'bloodbank_event',
            },
        ),
        migrations.CreateModel(
            name='Hospitals',
            fields=[
                ('h_id', models.AutoField(primary_key=True, serialize=False)),
                ('h_name', models.CharField(max_length=50)),
                ('h_address', models.CharField(max_length=300)),
                ('h_email', models.EmailField(max_length=254, unique=True)),
                ('h_pwd', models.CharField(max_length=15)),
                ('h_contact', models.CharField(max_length=15)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.area')),
            ],
            options={
                'db_table': 'bloodbank_hospital',
            },
        ),
        migrations.CreateModel(
            name='Receiver',
            fields=[
                ('receiver_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('Gender', models.BooleanField()),
                ('email', models.CharField(max_length=30)),
                ('dob', models.DateTimeField()),
                ('donor_weight', models.IntegerField()),
                ('contact_no', models.IntegerField()),
                ('id_proof', models.CharField(max_length=20)),
                ('home_number', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=8)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.area')),
                ('bloodgrp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.blood_grp')),
            ],
            options={
                'db_table': 'bloodbank_receiver',
            },
        ),
        migrations.CreateModel(
            name='Van',
            fields=[
                ('van_id', models.AutoField(primary_key=True, serialize=False)),
                ('van_num', models.IntegerField()),
                ('v_datetime', models.DateTimeField()),
                ('v_add', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=100)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.area')),
            ],
            options={
                'db_table': 'bloodbank_van',
            },
        ),
        migrations.CreateModel(
            name='Request_blood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_id', models.IntegerField()),
                ('status', models.BooleanField()),
                ('qty', models.IntegerField()),
                ('b_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.bloodbank')),
                ('bloodgrp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.blood_grp')),
                ('h_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.hospitals')),
                ('receiver_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.receiver')),
            ],
            options={
                'db_table': 'bloodbank_requestblood',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gallery_id', models.IntegerField()),
                ('img_path', models.CharField(max_length=50)),
                ('b_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.bloodbank')),
                ('event_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.event')),
                ('h_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.hospitals')),
            ],
            options={
                'db_table': 'bloodbank_gallery',
            },
        ),
        migrations.AddField(
            model_name='event',
            name='h_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.hospitals'),
        ),
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('d_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=10)),
                ('last_name', models.CharField(max_length=10)),
                ('Gender', models.BooleanField()),
                ('email', models.CharField(max_length=30)),
                ('dob', models.DateTimeField()),
                ('donor_weight', models.IntegerField()),
                ('contact_no', models.IntegerField()),
                ('id_proof', models.CharField(max_length=20)),
                ('home_number', models.CharField(max_length=5)),
                ('address', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=8)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.area')),
                ('bloodgrp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.blood_grp')),
            ],
            options={
                'db_table': 'bloodbank_donor',
            },
        ),
        migrations.CreateModel(
            name='Blood_stock',
            fields=[
                ('stock_id', models.AutoField(primary_key=True, serialize=False)),
                ('b_stock', models.IntegerField()),
                ('b_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.bloodbank')),
                ('bloodgrp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.blood_grp')),
            ],
            options={
                'db_table': 'bloodbank_bloodstock',
            },
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appointment_id', models.IntegerField()),
                ('given_date', models.DateTimeField()),
                ('appointment_status', models.BooleanField()),
                ('appointment_time', models.DateTimeField()),
                ('b_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.bloodbank')),
                ('d_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bbank_admin.donor')),
            ],
            options={
                'db_table': 'bloodbank_appointment',
            },
        ),
    ]
