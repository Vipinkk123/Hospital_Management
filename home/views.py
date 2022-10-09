from django.shortcuts import render
from django.http import HttpResponse

from .models import Department,Doc
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method== "POST":
        form=BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    form_dict={
        'form':form
    }
    return render(request, 'booking.html', form_dict)

def doctors(request):
    doc_dict={
        'doc': Doc.objects.all()
    }
    return render(request, 'doctors.html', doc_dict)

def contact(request):
    return render(request, 'contact.html') 

def department(request):
    dept_dict={
        'dept': Department.objects.all()
    }
    return render(request, 'department.html', dept_dict)

def simple(request):
    return HttpResponse("Simple Page")
 
