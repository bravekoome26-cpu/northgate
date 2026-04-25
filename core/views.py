from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import BookingForm, OrderForm, TableReservationForm, UserRegistrationForm
from .models import Booking, FoodItem, Order, Room, TableReservation


def home(request):
    rooms = Room.objects.filter(is_available=True).order_by('price')[:6]
    return render(request, 'core/home.html', {'rooms': rooms})


def about(request):
    return render(request, 'core/about.html')


def experiences(request):
    return render(request, 'core/experiences.html')


def events(request):
    return render(request, 'core/events.html')


def contact(request):
    return render(request, 'core/contact.html')


def packages(request):
    return render(request, 'core/packages.html')


def room_list(request):
    rooms = Room.objects.filter(is_available=True).order_by('price')
    return render(request, 'core/room_list.html', {'rooms': rooms})


def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = BookingForm()
    return render(request, 'core/room_detail.html', {'room': room, 'form': form})


@login_required
def book_room(request, pk):
    room = get_object_or_404(Room, pk=pk, is_available=True)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room = room
            days = (booking.check_out - booking.check_in).days
            if days <= 0:
                messages.error(request, 'Check-out date must be after check-in date.')
            else:
                booking.total_price = days * room.price
                booking.save()
                messages.success(request, 'Your room has been reserved successfully.')
                return redirect('booking_history')
    else:
        form = BookingForm()
    return render(request, 'core/room_detail.html', {'room': room, 'form': form})


@login_required
def booking_history(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'core/bookings.html', {'bookings': bookings})


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account was created successfully.')
            return redirect('home')
    else:
        form = UserRegistrationForm()
    return render(request, 'core/register.html', {'form': form})


def food_menu(request):
    food_items = FoodItem.objects.filter(available=True)
    return render(request, 'core/food_menu.html', {'food_items': food_items})


@login_required
def order_food(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            form.save_m2m()  # Save many-to-many relationships
            messages.success(request, 'Your food order has been placed successfully.')
            return redirect('order_history')
    else:
        form = OrderForm()
    return render(request, 'core/order_food.html', {'form': form})


@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'core/order_history.html', {'orders': orders})


@login_required
def table_reservation(request):
    if request.method == 'POST':
        form = TableReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            messages.success(request, 'Your table has been reserved successfully.')
            return redirect('home')
    else:
        form = TableReservationForm()
    return render(request, 'core/table_reservation.html', {'form': form})
