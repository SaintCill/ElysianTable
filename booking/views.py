from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import BookingForm, ContactForm
from .models import Booking
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')


def check_availability(date, time, guests):
    max_tables = 10  # Example: the restaurant has 10 tables
    existing_bookings = Booking.objects.filter(date=date, time=time)
    return len(existing_bookings) < max_tables




def book_table(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            name = cleaned_data['name']
            email = cleaned_data['email']
            phone = cleaned_data['phone']
            date = cleaned_data['date']
            time = cleaned_data['time']
            guests = cleaned_data['guests']
            special_requests = cleaned_data['special_requests']

            if check_availability(date, time, guests):
                Booking.objects.create(
                    name=name,
                    email=email,
                    phone=phone,
                    date=date,
                    time=time,
                    guests=guests,
                    special_requests=special_requests
                )
                messages.success(request, 'Table booked successfully!')
                return redirect('book_table')
            else:
                messages.error(request, 'No available tables at that time.')
        else:
            messages.error(request, 'Form data is not valid. Please check the inputs.')

    else:
        form = BookingForm()

    context = {
        'form': form
    }
    return render(request, 'book_table.html', context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_success')
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})