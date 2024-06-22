from django.shortcuts import render,redirect
from item.models import Category,Item

from .forms import SignupForm
# Create your views here.

def index(request):
    # Getting the item which is not sold ,the [0:6] only retrieves the first 6 instances
    items=Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()
    
    return render(request,'core/index.html',{
        'categories':categories,
        'items':items,
    })

def contact(request):
    return render(request,'core/contact.html')

def signup(request):
    if request.method=='POST':
        # Creating a instance of SignupForm
        form=SignupForm(request.POST)

        # Checking if the form is valid or not by running validation rules defined in the SignupForm
        if form.is_valid():
            # It saves the data, it involves creating a new user object in the database based on the form field(username,email,password)
            form.save()

            return redirect('/login/')
    else:
        form=SignupForm()
        
    return render(request,'core/signup.html',{
        'form':form
    })