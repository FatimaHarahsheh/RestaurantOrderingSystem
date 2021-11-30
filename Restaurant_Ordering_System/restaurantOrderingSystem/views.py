from django.shortcuts import render,redirect
from .models import  *
def index(request):
    context = {"category": Category.objects.all()}		
    return render(request, "index.html", context)

def invoice(request):
    context = {"invoice": Invoice.objects.all()}		
    return render(request, "invoice.html", context)

def Order(request):
    context = {"order": Order.objects.all()}		
    return render(request, "order.html", context)

def add_order(request):
    tableNumber = request.POST["tableNumber"] 
    quntity = request.POST["quntity"]
    numberOfinvoice = request.POST["numberOfinvoice"]
    order = Order.objects.create(tableNumber= tableNumber,quntity= quntity,numberOfinvoice = numberOfinvoice,)
    return redirect('/')


def order(request,id):
    context={
        'order' : Order.objects.get(id=id)
    }
    return render(request,'orders.html',context)

def invoice(request,id):
    context={
        'order' : Invoice.objects.get(id=id)
    }
    return render(request,'invoice.html',context)

