from django.shortcuts import render, redirect, reverse
from .models import Photo, Reservation
from .forms import ReservationForm
from django.contrib import messages
from datetime import datetime


def home(request):
    banner_image = Photo.objects.get(title='banner_image')
    about_image = Photo.objects.get(title='about_image')
    logo_image = Photo.objects.get(title='indian tuin_logo')
    context = {
        'banner_image': banner_image,
        'about_image': about_image}
    return render(request, 'home/index.html', context)


def reservations(request):
    """
    This view will render the reservations page
    """

    time_image = Photo.objects.get(title='Times Image')
    form = ReservationForm()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        date = form['date'].value()
        date_value = datetime.strptime(date, '%m/%d/%Y')
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation created successfully.')
            return redirect('restaurant:reservations')
        else:
            messages.error(request, f'Some details are missing/wrong. {form.errors}')
    context = {
        'time_image': time_image,
        'form': form
    }
    return render(request, 'home/reservations.html', context)


def edit_user_reservation(request, slug):
    reservation = Reservation.objects.get(slug=slug)
    form = ReservationForm(instance=reservation)

    if request.method == 'POST':
        form = ReservationForm(
            request.POST, request.FILES,
            instance=reservation
            )
        if form.is_valid():
            form.save()
            messages.success(request, 'Reservation Updated.')
            return redirect('restaurant:reservations')

    context = {'form': form}
    return render(request, 'home/edit_reservation.html', context)


def delete_user_reservation(request, slug):
    reservation = Reservation.objects.get(slug=slug)

    if request.method == 'POST':
        reservation.delete()
        messages.success(request, 'Reservation has been deleted.')

    context = {'reservation': reservation}
    return render(request, 'home/delete_reservation.html', context)
