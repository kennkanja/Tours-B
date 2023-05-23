from django.forms import ModelForm, Textarea
from .models import Reservation

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ["dest","fname","email","pno","sdate","fdate","gender","country","city","no_child","no_adults"]
        widgets ={
            
            "dest" : Textarea(attrs={"cols" : 40, "rows" : 2}),
            "fname" : Textarea(attrs={"cols" : 40, "rows" : 2}),
            "email" : Textarea(attrs={"cols" : 40, "rows" : 2}),
            "pno" : Textarea(attrs={"cols" : 40, "rows" : 2}),
            "sdate" : Textarea(attrs={"cols" : 40, "rows" : 2}),
            "fdate" : Textarea(attrs={"cols" : 40, "rows" : 2}),
            "gender" : Textarea(attrs={"cols" : 40, "rows" : 2}),
            "country" : Textarea(attrs={"cols" : 40, "rows" : 2}),
            "city" : Textarea(attrs={"cols" : 40, "rows" : 2}),
            "no_child" : Textarea(attrs={"cols" : 40, "rows" : 2}),
            "no_adults" : Textarea(attrs={"cols" : 40, "rows" : 2}),
         }
        labels ={
            "dest": ("Place you want to Visit :"),
            "fname": ("Enter your Full Name   :"),
            "email": ("Enter your Email Address :"),
            "pno": ("Enter your Phone Number:"),
            "sdate": ("Enter the Start Date   :"),
            "fdate": ("Enter the Final Date   :"),
            "gender": ("Enter you preferred gender:"),
            "country": ("Enter Country of Origin :"),
            "city":("Enter City of of Origin :"),
            "no_child":("Enter no of children traveling :"),
            "no_adults":("Enter no of adults traveling :")
        }