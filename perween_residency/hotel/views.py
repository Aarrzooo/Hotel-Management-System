from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages


from .models import Booking, Contact, Customer


def home(request):

    customer = None

    if "customer_id" in request.session:
        customer = Customer.objects.get(id=request.session["customer_id"])

    return render(request, "index.html", {"customer": customer})

def about(request):

    customer = None

    if "customer_id" in request.session:
        customer = Customer.objects.get(id=request.session["customer_id"])

    return render(request, "about.html", {"customer": customer})


def rooms(request):

    customer = None

    if "customer_id" in request.session:
        customer = Customer.objects.get(id=request.session["customer_id"])

    return render(request, "rooms.html", {"customer": customer})


def booking(request):

    customer = None

    if "customer_id" in request.session:
        customer = Customer.objects.get(id=request.session["customer_id"])

    if request.method == "POST":

        if not customer:
            messages.warning(request, "Please login first to book your room.")
            return redirect("booking")

        Booking.objects.create(
            name=customer.name,
            email=customer.email,
            phone=customer.phone,
            room_type=request.POST["room_type"],
            guests=request.POST["guests"],
            check_in=request.POST["check_in"],
            check_out=request.POST["check_out"],
        )

        messages.success(request, "Booking Confirmed Successfully!")
        return redirect("booking")

    return render(request, "booking.html", {"customer": customer})

def contact(request):

    customer = None

    if request.method == "POST":

        Contact.objects.create(
            name=request.POST["name"],
            email=request.POST["email"],
            subject=request.POST["subject"],
            message=request.POST["message"]
        )

        return redirect("contact")

    if "customer_id" in request.session:
        customer = Customer.objects.get(id=request.session["customer_id"])

    return render(request, "contact.html", {"customer": customer})

def customer_login(request):

    if request.method == "POST":

        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        address = request.POST.get("address")

        customer, created = Customer.objects.get_or_create(
            email=email,
            defaults={
                "name": name,
                "phone": phone,
                "address": address
            }
        )

        customer.name = name
        customer.phone = phone
        customer.address = address
        customer.save()

        request.session["customer_id"] = customer.id

        messages.success(request, "Login Successful! Now you can book your room.")
    return redirect(request.META.get("HTTP_REFERER", "home"))


    
def logout_user(request):

    request.session.flush()

    return redirect("home")
