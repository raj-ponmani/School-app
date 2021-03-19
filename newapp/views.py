from django.shortcuts import render
#from django.http import HttpResponse
from .models import destination
# Create your views here.
def index(request):

    return render(request, 'index.html')

def form(request):
    return render(request, 'form.html')

def result(request):
    if request.method=="POST":
        studentname = request.POST['studentname']
        fathername = request.POST['fathername']
        paddress = request.POST['paddress']
        personaladdress = request.POST['personaladdress']
        sex = request.POST['sex']
        City = request.POST['City']
        Course = request.POST['Course']
        pincode = request.POST['pincode']
        emailid = request.POST['emailid']
        dob = request.POST['dob']
        mobileno = request.POST['mobileno']
        #print(studentname,fathername,paddress,personaladdress,sex,City,Course,pincode,emailid,dob,mobileno)
        ins = destination(
        Student_Name=studentname,
        Father_Name = fathername,
        Postal_address = paddress,
        Personal_Address = personaladdress,
        Sex = sex,
        City = City,
        Course = Course,
        Pincode = pincode,
        EmailID = emailid,
        DOB = dob,
        MobileNO = mobileno,
        )
        ins.save()
        print("The data has been written to the DATABASE")

    return render(request, 'result.html')

"""
use this incase city field show an error...

if request.POST.get('City'):
    City = destination #this class is from models
    City = request.POST.get('City')"""