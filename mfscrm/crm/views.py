from django.shortcuts import render,get_object_or_404, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

now = timezone.now()
def home(request):
   return render(request, 'crm/home.html',
                 {'crm': home})

@login_required
def customer_list(request):
    customer = Customer.objects.filter(created_date__lte=timezone.now())
    return render(request, 'crm/customer_list.html',
                 {'customers': customer})

@login_required
def customer_edit(request, pk):
   name = 'Edit'
   customer = get_object_or_404(Customer, pk=pk)
   if request.method == "POST":
       # update
       form = CustomerForm(request.POST, instance=customer)
       if form.is_valid():
           customer = form.save(commit=False)
           customer.updated_date = timezone.now()
           customer.save()
           customer = Customer.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/customer_list.html',
                         {'customers': customer})
   else:
        # edit
       form = CustomerForm(instance=customer)
   return render(request, 'crm/customer_edit.html', {'form': form, 'name': name})


@login_required
def customer_delete(request, pk):
   customer = get_object_or_404(Customer, pk=pk)
   customer.delete()
   return redirect('crm:customer_list')


@login_required
def customer_new(request):
    name = 'Add'
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save(commit=False)
            customer.created_date = timezone.now()
            customer.save()
            customer = Customer.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/customer_list.html', {'customers': customer})
    else:
        form = CustomerForm()
    return render(request, 'crm/customer_edit.html', {'form': form, 'name': name})

@login_required
def service_list(request):
   services = Service.objects.filter(created_date__lte=timezone.now())
   return render(request, 'crm/service_list.html', {'services': services})

@login_required
def service_new(request):
   name = 'Add a new Service'
   if request.method == "POST":
       form = ServiceForm(request.POST)
       if form.is_valid():
           service = form.save(commit=False)
           service.created_date = timezone.now()
           service.save()
           services = Service.objects.filter(created_date__lte=timezone.now())
           return render(request, 'crm/service_list.html',
                         {'services': services})
   else:
       form = ServiceForm()
       # print("Else")
   return render(request, 'crm/service_new.html', {'form': form, 'name': name})


@login_required
def service_edit(request, pk):
    service = get_object_or_404(Service, pk=pk)
    name = 'Edit Service: '+ str(service.cust_name)
    if request.method == 'POST':
        form = ServiceForm(request.POST, instance= service)
        if form.is_valid():
            service = form.save(commit=False)
            service.updated_date = timezone.now()
            service.save()
            services = Service.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/service_list.html', {'services': services})
    else:
        form = ServiceForm(instance=service);
    return render(request, 'crm/service_new.html', {'form': form, 'name': name})

@login_required
def service_delete(request, pk):
    service = get_object_or_404(Service, pk=pk)
    service.delete()
    return redirect('crm:service_list')



@login_required
def product_list(request):
    products = Product.objects.filter(created_date__lte=timezone.now())
    dictionary = {'products': products}
    return render(request, 'crm/product_list.html', dictionary)

@login_required
def product_create(request):
    name = 'Add a Product '
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.updated_date = timezone.now()
            product.save()
            products = Product.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/product_list.html', {'products': products})
    else:
        form = ProductForm()
    return render(request, 'crm/product_form.html', {'form': form, 'name': name})

@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)
    product.delete()
    return redirect('crm:product_list')

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    name = 'Edit Product: ' + str(product.cust_name) + ' ' + str(product.product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.updated_date = timezone.now()
            product.save()
            products = Product.objects.filter(created_date__lte=timezone.now())
            return render(request, 'crm/product_list.html', {'products': products})
    else:
        form = ProductForm(instance=product)
    return render(request, 'crm/product_form.html', {'form': form, 'name': name})


