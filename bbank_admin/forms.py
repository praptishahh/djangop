from bbank_admin.models import Area
from bbank_admin.models import Blood_grp
from bbank_admin.models import Donor
from bbank_admin.models import Receiver
from bbank_admin.models import Bloodbank
from bbank_admin.models import Hospitals
from bbank_admin.models import Blood_stock
from bbank_admin.models import Appointment
from bbank_admin.models import Request_blood
from bbank_admin.models import Event
from django import forms


#class UserForm(forms.ModelForm):
 #   class Meta:
  #      model = User
   #     fields = ["u_id", "u_name", "u_email", "u_contact", "u_pwd", "otp", "otp_used", "area_id", "is_admin"]


class AreaForm(forms.ModelForm):
    class Meta:
        model = Area
        fields = ["area_id", "area_name", "pincode"]


class Blood_grpForm(forms.ModelForm):
    class Meta:
        model = Blood_grp
        fields = ["bloodgrp_id", "bloodgrp_type"]


class DonorForm(forms.ModelForm):
    class Meta:
        model = Donor
        fields = ["d_id", "first_name", "last_name", "bloodgrp_id", "Gender", "email", "dob", "donor_weight", "contact_no", "id_proof", "home_number", "address", "state", "username", "password", "area_id"]


class ReceiverForm(forms.ModelForm):
    class Meta:
        model = Receiver
        fields = ["receiver_id", "first_name", "last_name", "bloodgrp_id", "Gender", "email", "dob", "donor_weight", "contact_no", "id_proof", "home_number", "address", "state", "username", "password", "area_id"]


class BloodbankForm(forms.ModelForm):
    class Meta:
        model = Bloodbank
        fields = ["b_id", "b_name", "b_address", "b_email", "b_pwd", "b_contact", "b_timing", "area_id"]


class HospitalsForm(forms.ModelForm):
    class Meta:
        model = Hospitals
        fields = ["h_id", "h_name", "h_address", "h_email", "h_pwd", "h_contact", "area_id"]

class Blood_stockForm(forms.ModelForm):
    class Meta:
        model = Blood_stock
        fields = ["stock_id", "bloodgrp_id", "b_stock", "b_id"]

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ["appointment_id", "d_id", "given_date", "b_id", "appointment_status", "appointment_time"]


class Request_bloodForm(forms.ModelForm):
    class Meta:
        model = Request_blood
        fields = ["request_id", "receiver_id", "h_id", "bloodgrp_id", "b_id", "status", "qty"]


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ["event_id", "e_name", 'e_date', 'b_id', 'e_des', 'e_img', 'e_location', 'h_id', 'area_id']