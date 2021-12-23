from django.shortcuts import render, redirect
from bbank_admin.forms import AreaForm
from bbank_admin.models import Area
from bbank_admin.models import Blood_grp
from bbank_admin.forms import Blood_grpForm
from bbank_admin.models import Donor
from bbank_admin.forms import DonorForm
from bbank_admin.models import Receiver
from bbank_admin.forms import ReceiverForm
from bbank_admin.models import Bloodbank
from bbank_admin.forms import BloodbankForm
from bbank_admin.models import Hospitals
from bbank_admin.forms import HospitalsForm
from bbank_admin.models import Blood_stock
from bbank_admin.forms import Blood_stockForm
from bbank_admin.models import Appointment
from bbank_admin.forms import AppointmentForm
from bbank_admin.models import Request_blood
from bbank_admin.forms import Request_bloodForm
from bbank_admin.models import Admin
from bbank_admin.models import Event
from bbank_admin.models import Feedback
from bbank_admin.models import Gallery
from bbank_admin.models import Van
import random
import sys
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponse


def show_area(request):
    area = Area.objects.all()
    return render(request, "show_area.html", {'areas': area})


def show_bgrp(request):
    bgrp = Blood_grp.objects.all()
    return render(request, "show_bgrp.html", {'bgrps': bgrp})


def show_donor(request):
    donor = Donor.objects.all()
    return render(request, "show_donor.html", {'donors': donor})


def show_receiver(request):
    receiver = Receiver.objects.all()
    return render(request, "show_receiver.html", {'receivers': receiver})


def show_bbank(request):
    bbank = Bloodbank.objects.all()
    return render(request, "show_bbank.html", {'bbanks': bbank})


def show_hospital(request):
    hosp = Hospitals.objects.all()
    return render(request, "show_hospital.html", {'hospp': hosp})


def show_stock(request):
    stock = Blood_stock.objects.all()
    return render(request, "show_stock.html", {'stocks': stock})


def show_appointment(request):
    appointment = Appointment.objects.all()
    return render(request, "show_appointment.html", {'appointments ': appointment})


def show_requestblood(request):
    request_blood = Request_blood.objects.all()
    return render(request, "show_requestblood.html", {'request_bloods': request_blood})


def show_events(request):
    event = Event.objects.all()
    return render(request, "show_events.html", {'events': event})


def show_van(request):
    van = Van.objects.all()
    return render(request, "show_van.html", {'vans': van})


def show_gallery(request):
    gallery = Gallery.objects.all()
    return render(request, "show_gallery.html", {"gallerys": gallery})


def show_feedback(request):
    feedback = Feedback.objects.all()
    return render(request, "show_feedback.html", {"feedbacks": feedback})


def area_form(request):
    return render(request, "area_form.html")


def appointment_form(request):
    return render(request, "appointment_form.html")


def bgrp_form(request):
    return render(request, "bloodgrp_form.html")


def events_form(request):
    return render(request, "events.html")


def feedback_form(request):
    return render(request, "feedback_form.html")


def gallery_form(request):
    return render(request, "gallery_form.html")


def requestblood_form(request):
    return render(request, "bloodrequest_form.html")


def stock_form(request):
    return render(request, "bloodstock_form.html")


def van_form(request):
    return render(request, "vanscheduling_form.html")

def insert_area(request):
    if request.method == "POST":
        form = AreaForm(request.POST)
        print("----------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_area')
            except:
                print("---------", sys.exc_info())
    else:
        form = AreaForm()
    return render(request, 'area_form.html', {'form': form})

def destroy_area(request, area_id):
    area = Area.objects.get(area_id = area_id)
    area.delete()
    return redirect("/show_area")

def update_area(request, id):
    area = Area.objects.get(area_id=id)
    form = AreaForm(request.POST, instance=area)
    if form.is_valid():
        form.save()
        return redirect("/show_area")
    return render(request, 'edit_area.html', {'area': area})

def select_area(request, id):
    area = Area.objects.get(area_id=id)
    return render(request, 'edit_area.html', {'area': area})


def insert_bloodgrp(request):
    if request.method == "POST":
        form = Blood_grpForm(request.POST)
        print("----------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_bgrp')
            except:
                print("---------", sys.exc_info())
    else:
        form = Blood_grpForm()
    return render(request, 'bloodgrp_form.html', {'form': form})

def destroy_bloodgrp(request, bloodgrp_id):
    bgrp = Blood_grp.objects.get(bloodgrp_id = bloodgrp_id)
    bgrp.delete()
    return redirect("/show_bgrp")

def insert_stock(request):
    temp = Blood_grp.objects.all()
    flag = Bloodbank.objects.all()
    if request.method == "POST":
        form = Blood_stockForm(request.POST)
        print("----------", form.errors)
        if form.is_valid():
            try:
                form.save()
                return redirect('/show_stock')
            except:
                print("---------", sys.exc_info())
    else:
        form = Blood_stockForm()
    return render(request, 'bloodstock_form.html', {'form': form, 'temp': temp, 'flag': flag})

def destroy_stock(request, stock_id):
    stock = Blood_stock.objects.get(stock_id = stock_id)
    stock.delete()
    return redirect("/show_stock")


def login(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        val = Admin.objects.filter(admin_email=email, admin_password=password, is_admin=1).count()
        print("------------------", email, "-----------------", password)
        if val == 1:
            data = Admin.objects.filter(admin_email=email, admin_password=password, is_admin=1)
            for item in data:
                request.session['a_email'] = item.admin_email
                request.session['a_pw'] = item.admin_password
        else:
            messages.error(request, "Invalid user name and password")
            return redirect('/login')
    else:
        return render(request, "login.html")


def forgot(request):
    return render(request, 'passcode-reset.html')


def send_otp(request):
    otp1 = random.randint(10000, 99999)
    e = request.POST['email']

    request.session['temail'] = e

    obj = Admin.objects.filter(admin_email=e).count()

    if obj == 1:
        val = Admin.objects.filter(admin_email=e).update(otp=otp1, otp_used=0)

        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'set_password.html')


def set_password(request):
    if request.method == "POST":

        T_otp = request.POST['otp']
        T_pass = request.POST['admin_password']
        T_cpass = request.POST['cpass']

        if T_pass == T_cpass:

            e = request.session['temail']
            val = Admin.objects.filter(admin_email=e, otp=T_otp, otp_used=0).count()

            if val == 1:
                Admin.objects.filter(admin_email=e).update(otp_used=1, admin_password=T_pass)
                return redirect("/login")
            else:
                messages.error(request, "Invalid OTP")
                return render(request, "passcode-reset.html")

        else:
            messages.error(request, "New password and Confirm password does not match ")
            return render(request, "set_password.html")

    else:
        return redirect("/passcode-reset")
