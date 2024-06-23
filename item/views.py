from django.contrib.auth.decorators import login_required
from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,Category
from django.db.models import Q

from .forms import NewItemForm,EditItemForm

# Create your views here.
def items(request):
    query=request.GET.get('query','')
    categories=Category.objects.all()
    category_id=request.GET.get('category',0)
    items=Item.objects.filter(is_sold=False)

    # if category_id:
    #     try:
    #         category=Category.objects.get(pk=category_id)
    #         items=items.filter(category=category)
    #     # items=items.filter(category_id==category_id)
    #     except Category.DoesNotExist:
    #         pass

    if query:
        items=items.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request,'item/items.html',{
        'items':items,
        'query':query,
        'categories':categories,
        'category_id':int(category_id)
    })


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
    if request.method=='POST':
        form=NewItemForm(request.POST,request.FILES)

        if form.is_valid():
            # We commit the form save to false bcz the created_by field is not added
            item=form.save(commit=False)

            item.created_by=request.user

            item.save()

            return redirect('item:detail',pk=item.id)
    else:
        form=NewItemForm()

    return render(request,'item/form.html',{
        'form':form
    })

@login_required
def edit(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)


    if request.method=='POST':
        form=EditItemForm(request.POST,request.FILES,instance=item)

        if form.is_valid():
            # We commit the form save to false bcz the created_by field is not added
            form.save()

            return redirect('item:detail',pk=item.id)
    else:
        form=EditItemForm(instance=item)

    return render(request,'item/form.html',{
        'form':form
    })

@login_required
def delete(request,pk):
    item=get_object_or_404(Item,pk=pk,created_by=request.user)
    item.delete()

    return redirect('dashboard:index')