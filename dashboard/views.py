
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import *
from .models import *

# Create your views here.


def home(request):
    return render(request, 'dashboard/index.html')


def orders(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        # form = OrderForm()
        return redirect('/stats')
    context = {
        'form': form,
        'title': 'New Invoice'
    }

    return render(request, 'dashboard/order.html', context)

def updateOrder(request, pk):
    order = Order.objects.get(id = pk)
    create_order = OrderForm(instance=order)

     # save form
    if request.method == 'POST':
        create_order = OrderForm(request.POST, instance=order)
        if create_order .is_valid():
            create_order.save()
            return redirect('/')

    cnx = {'create_order': create_order}

    return render(request, 'order.html', cnx)


def stats(request):
    orders = Order.objects.all()
    pending = Order.objects.filter(status='Pending').count()
    delivered = Order.objects.filter(status='Delivered').count()
    total_orders = Order.objects.count()
    products = Product.objects.all()
    customers = Customer.objects.all()
    context = {'orders': orders, 'pending': pending,
               'delivered': delivered, 'customers': customers, 'products': products, 'total_orders': total_orders}
    return render(request, 'dashboard/stats.html', context)


def customers(request):
    customers = Customer.objects.all()
    total_customers = Customer.objects.count()
    total_orders = Order.objects.count()
    total_products = Product.objects.count()

    context = {'customers': customers, 'total_orders': total_orders, 'total_customers': total_customers,
               'total_products': total_products}

    return render(request, 'dashboard/customers.html', context)

def customer_reg(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form': form,

    }

    return render(request, 'dashboard/customer_reg.html', context)



