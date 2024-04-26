from typing import Any
from django.shortcuts import render,redirect
from django.views.generic import ListView,TemplateView

from .models import Food,Appointment,Qoute

from django.contrib import messages
# Create your views here.


def home(request):
        all_foods=Food.objects.all()
        all_quotes=Qoute.objects.all()
        

        data={
            'foods': all_foods,
            'all_quotes':all_quotes,
            }
    

        return render(request,'index.html',context=data)

class Home(TemplateView):
    template_name='index.html'
    
    def get_context_data(self,*args, **kwargs):
        
            all_foods=Food.objects.all()
            data={
                  'all_foods':all_foods,
                  
                  }
            return data


class Qoutes(TemplateView):
    template_name='qoutes.html'

    def get_context_data(self,*args, **kwargs):
        
            all_qoutes=Qoute.objects.all()
            data={
                  'all_qoutes':all_qoutes,
                  
                  }
            return data

    def  post(self,request):
        qname=request.POST.get('name')
        qemail=request.POST.get('email')
        qquote=request.POST.get('quote')

        comment=Qoute.objects.create(
            name=qname,
            email=qemail,
            quote=qquote
        )

        comment.save()
        messages.success(request,"comment saved succesfully")
        
        return redirect('home')

class Book(TemplateView):
    template_name='book.html'
    

    def post(self,request):
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        phone=request.POST.get('phone')
        number_of_guest=request.POST.get('number_of_guest')
        date=request.POST.get('date')
        
        

        appointment=Appointment.objects.create(
        name=name,
        email=email,
        phone=phone,
        message=message,
        number_of_guests=number_of_guest,
        date=date,
        
    )    
        appointment.save()
        messages.success(request,"Your Reservation Saved Succesfully,We will contact yous soon")
        return redirect('home')
    

class Menu(ListView):
     template_name='menu.html'
     model=Food

     context_object_name='menu'


class About(TemplateView):
     template_name='about.html'
     


