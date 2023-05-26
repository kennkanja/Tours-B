from django.forms import ModelForm, Textarea
from .models import Reservation, Contact

class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ["dest","fname","email","pno","sdate","fdate","gender","country","city","no_child","no_adults"]
        widgets ={
            
            "dest" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Place to Visit","style":'width: 300px;',"class":"form-control"}),
            "fname" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Enter Full Name ","style":'width: 300px;',"class":"form-control"}),
            "email" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Enter Email Address","style":'width: 300px;',"class":"form-control"}),
            "pno" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Enter Phone Number","style":'width: 300px;',"class":"form-control"}),
            "sdate" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Enter Start Date of Tour  yy-mm-dd","style":'width: 300px;',"class":"form-control"}),
            "fdate" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Enter Last Date of Tour yy-mm-dd","style":'width: 300px;',"class":"form-control"}),
            "gender" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Enter Your Preferred Gender","style":'width: 300px;',"class":"form-control"}),
            "country" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Place to Visit","style":'width: 300px;',"class":"form-control"}),
            "city" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Enter City of Origin","style":'width: 300px;',"class":"form-control"}),
            "no_child" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Enter the Number  of Children  Travelling","style":'width: 300px;',"class":"form-control"}),
            "no_adults" : Textarea(attrs={"cols" : 40, "rows" : 2, "placeholder" : "Enter the Number  of Children  Travelling","style":'width: 300px;',"class":"form-control"}),
         }
        labels ={
            "dest":("Destination :"),
            "fname":("Full Name :"),
            "email":("Email Address:"),
            "pno": ("Phone Number:"),
            "sdate": ("Start Date:"),
            "fdate": ("Final Date:"),
            "gender": ("Enter Gender:"),
            "country":("Country of Origin :"),
            "city":("City of Origin:"),
            "no_child":("No of children:"),
            "no_adults":("No of adults:")
        }

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ["name","email","phone","subject"]