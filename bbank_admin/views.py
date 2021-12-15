from django.shortcuts import render, redirect
#from bbank_admin.models import User
#from bbank_admin.forms import AreaForm
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
import random
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
    donor=Donor.objects.all()
    return render(request, "show_donor.html", {'donors': donor})


def show_receiver(request):
    receiver=Receiver.objects.all()
    return render(request, "show_receiver.html", {'receivers': receiver})


def show_bbank(request):
    bbank=Bloodbank.objects.all()
    return render(request, "show_bbank.html", {'bbanks': bbank})


def show_hospital(request):
    hosp=Hospitals.objects.all()
    return render(request, "show_hospital.html", {'hospp': hosp})


def show_stock(request):
    stock=Blood_stock.objects.all()
    return render(request, "show_stock.html", {'stocks': stock})

def show_appoinment(request):
    appoinment = Appointment.objects.all()
    return render(request, "show_appoinment.html", {'appoinments ': appoinment})


def show_requestblood(request):
     request_blood= Request_blood.objects.all()
     return render(request, "show_requestblood.html", {'request_bloods': request_blood})


def show_form1(request):
    return render(request, "header_footer_forms.html")


def login(request):
    if request.method=="POST":
        email=request.POST["email"]
        password=request.POST["password"]
        val=Admin.objects.filter(admin_email=email,admin_password=password).count()
        print("------------------",email,"-----------------",password)
        if val == 1:
	        data=Admin.objects.filter(admin_email=email,admin_password=password)
	        for item in data:
		        request.session['admin_email']=item.email
		        request.session['admin_pw']=item.password
        else:
            messages.error(request, "Invalid user name and password")
            return redirect('/login/')
    else:
        return render(request,"login.html")


def forgot(request):
    return render(request,'forgotpassword.html')

def send_otp(request):

    otp1 = random.randint(10000, 99999)
    e = request.POST['email']

    request.session['temail']=e

    obj = Admin.objects.filter(admin_email=e).count()

    if obj == 1:

        val = Admin.objects.filter(admin_email=e).update(otp=otp1 , otp_used=0)

        subject = 'OTP Verification'
        message = str(otp1)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [e, ]

        send_mail(subject, message, email_from, recipient_list)

        return render(request, 'set_password.html')