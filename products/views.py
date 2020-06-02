from django.shortcuts import render, HttpResponse, redirect, get_object_or_404, reverse
from .forms import ProductForm
from .models import Product, organization
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def products(request):
    keyword = request.GET.get("keyword")

    if keyword:
        products = Product.objects.filter(title__contains=keyword)
        return render(request, "products.html", {"products": products})
    products = Product.objects.all()

    return render(request, "products.html", {"products": products})

def organizationsngo(request):
    keyword = request.GET.get("keyword")

    if keyword:
        organizations = organization.objects.filter(title__contains=keyword)
        return render(request, "organizations.html", {"organizations": organizations})

    organizations = organization.objects.filter(type = '0')

    return render(request, "organizations.html", {"organizations": organizations})

def organizationsgo(request):
    keyword = request.GET.get("keyword")

    if keyword:
        organizations = organization.objects.filter(title__contains=keyword)
        return render(request, "organizations.html", {"organizations": organizations})

    organizations = organization.objects.filter(type = '1')

    return render(request, "organizations.html", {"organizations": organizations})

def organizationsother(request):
    keyword = request.GET.get("keyword")

    if keyword:
        organizations = organization.objects.filter(title__contains=keyword)
        return render(request, "organizations.html", {"organizations": organizations})

    organizations = organization.objects.filter(type = '2')

    return render(request, "organizations.html", {"organizations": organizations})

def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def register(request):
    return(request, "register.html")

@login_required(login_url="user:login")
def dashboard(request):
    products = Product.objects.filter(author=request.user)
    context = {
        "products": products,
    }
    return render(request, "dashboard.html", context)


@login_required(login_url="user:login")
def addProduct(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        product = form.save(commit=False)

        product.author = request.user
        product.save()

        messages.success(request, "Product Created Successfully!!!")
        return redirect("products:dashboard")
    return render(request, "addproduct.html", {"form": form})


def detail(request, id):
    #product = Product.objects.filter(id = id).first()
    product = get_object_or_404(Product, id=id)

    return render(request, "product_detail.html", {"products": product})

@login_required(login_url="user:login")
def updateProduct(request, id):
    product = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, request.FILES or None, instance=product)
    if form.is_valid():
        product = form.save(commit=False)

        product.author = request.user
        product.save()

        messages.success(request, "Product Successfully Updated")
        return redirect("products:dashboard")

    return render(request, "update.html", {"form": form})


@login_required(login_url="user:login")
def deleteProduct(request, id):
    product = get_object_or_404(Product, id=id)

    product.delete()

    messages.success(request, "Product Successfully Deleted")

    return redirect("products:dashboard")



