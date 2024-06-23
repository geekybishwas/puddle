from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404
from .models import Item

from .forms import NewItemForm

# Create your views here.
def detail(request,pk):
    # pk(this is the primary key from the model itself)=pk(this is the primary key from the parameters)
    # It not found it gives 404 error
    item=get_object_or_404(Item,pk=pk)
    # It is getting the related items from the items whose category matches the item category,is_sold=False and also exclude the item whose primary key is pk
    related_items=Item.objects.filter(category=item.category,is_sold=False).exclude(pk=pk)
    return render(request,'item/detail.html',{
        'item':item,
        'related_items':related_items
    })

@login_required
def new(request):
    form=NewItemForm()

    return render(request,'item/form.html',{
        'form':form
    })