from django.db import models


# Create your models here.


class Area(models.Model):
    area_id = models.AutoField(primary_key=True)
    area_name = models.CharField(max_length=150, null=False)
    pincode = models.CharField(max_length=6)

    class Meta:
        db_table = "bloodbank_area"


class Bloodbank(models.Model):
    b_id = models.AutoField(primary_key=True)
    b_name = models.CharField(max_length=50)
    b_address = models.CharField(max_length=300, null=False)
    b_email = models.EmailField(unique=True)
    b_pwd = models.CharField(max_length=15)
    b_contact = models.CharField(max_length=15)
    b_timing = models.DateTimeField()
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        db_table = "bloodbank_bloodbank"


class Hospitals(models.Model):
    h_id = models.AutoField(primary_key=True)
    h_name = models.CharField(max_length=50)
    h_address = models.CharField(max_length=300)
    h_email = models.EmailField(unique=True)
    h_pwd = models.CharField(max_length=15)
    h_contact = models.CharField(max_length=15)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        db_table = "bloodbank_hospital"


class Event(models.Model):
    event_id = models.AutoField(primary_key=True)
    e_name = models.CharField(max_length=100)
    e_date = models.DateField()
    b_id = models.ForeignKey(Bloodbank, on_delete=models.CASCADE)
    e_des = models.CharField(max_length=500)
    e_img = models.ImageField()
    e_location = models.CharField(max_length=200)
    h_id = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        db_table = "bloodbank_event"


class Blood_grp(models.Model):
    bloodgrp_id = models.AutoField(primary_key=True)
    bloodgrp_type = models.CharField(max_length=5)

    class Meta:
        db_table = "bloodbank_bloods_grp"


class Blood_stock(models.Model):
    stock_id = models.AutoField(primary_key=True)
    bloodgrp_id = models.ForeignKey(Blood_grp, on_delete=models.CASCADE)
    b_stock = models.IntegerField()
    b_id = models.ForeignKey(Bloodbank, on_delete=models.CASCADE)

    class Meta:
        db_table = "bloodbank_bloodstock"


class Van(models.Model):
    van_id = models.AutoField(primary_key=True)
    van_num = models.IntegerField()
    v_datetime = models.DateTimeField()
    v_add = models.CharField(max_length=300)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)

    class Meta:
        db_table = "bloodbank_van"


class Donor(models.Model):
    d_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    bloodgrp_id = models.ForeignKey(Blood_grp, on_delete=models.CASCADE)
    Gender = models.BooleanField()
    email = models.CharField(max_length=30)
    dob = models.DateTimeField()
    donor_weight = models.IntegerField()
    contact_no = models.IntegerField()
    id_proof = models.CharField(max_length=20)
    home_number = models.CharField(max_length=5)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        db_table = "bloodbank_donor"


class Receiver(models.Model):
    receiver_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)
    bloodgrp_id = models.ForeignKey(Blood_grp, on_delete=models.CASCADE)
    Gender = models.BooleanField()
    email = models.CharField(max_length=30)
    dob = models.DateTimeField()
    donor_weight = models.IntegerField()
    contact_no = models.IntegerField()
    id_proof = models.CharField(max_length=20)
    home_number = models.CharField(max_length=5)
    address = models.CharField(max_length=100)
    state = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=8)
    area_id = models.ForeignKey(Area, on_delete=models.CASCADE)

    class Meta:
        db_table = "bloodbank_receiver"


class Appointment(models.Model):
    appointment_id = models.IntegerField()
    d_id = models.ForeignKey(Donor, on_delete=models.CASCADE)
    given_date = models.DateTimeField()
    b_id = models.ForeignKey(Bloodbank, on_delete=models.CASCADE)
    appointment_status = models.BooleanField()
    appointment_time = models.DateTimeField()

    class Meta:
        db_table = "bloodbank_appointment"


class Request_blood(models.Model):
    request_id = models.IntegerField()
    receiver_id = models.ForeignKey(Receiver, on_delete=models.CASCADE)
    h_id = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    bloodgrp_id = models.ForeignKey(Blood_grp, on_delete=models.CASCADE)
    b_id = models.ForeignKey(Bloodbank, on_delete=models.CASCADE)
    status = models.BooleanField()
    qty = models.IntegerField()

    class Meta:
        db_table = "bloodbank_requestblood"


class Gallery(models.Model):
    gallery_id = models.IntegerField()
    b_id = models.ForeignKey(Bloodbank, on_delete=models.CASCADE)
    h_id = models.ForeignKey(Hospitals, on_delete=models.CASCADE)
    img_path = models.CharField(max_length=50)
    event_id = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        db_table = "bloodbank_gallery"


class Admin(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=100)
    admin_email = models.EmailField(unique=True)
    admin_contact = models.CharField(max_length=15)
    admin_password = models.CharField(max_length=15)
    otp = models.CharField(max_length=10, null=True)
    otp_used = models.IntegerField()

    class Meta:
        db_table="admin"
