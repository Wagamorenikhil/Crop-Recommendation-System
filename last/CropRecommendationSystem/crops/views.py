from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Season, Crop
from .forms import SeasonForm, CropForm # type: ignore

def home(request):
    seasons = Season.objects.all()
    return render(request, 'crops/home.html', {'seasons': seasons})

def base(request):
    return render(request, 'crops/base.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Admin,User

def login_admin(request):
    if request.method == 'POST':
        username = request.POST.get('admin')
        password = request.POST.get('password')
        
        try:
            admin = Admin.objects.get(A_name=username)
            if admin.A_pwd == password:
                # Assuming you are not using Django's built-in User model for authentication
                # Instead, create a session for the logged-in admin
                request.session['admin_id'] = admin.id
                return redirect('home')  # Replace 'home' with your actual home page name
            else:
                messages.error(request, 'Invalid username or password.')
        except Admin.DoesNotExist:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'crops/login_admin.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(U_name=username)
            if user.U_pwd == password:
                # Assuming you are not using Django's built-in User model for authentication
                # Instead, create a session for the logged-in admin
                request.session['admin_id'] = user.id
                return redirect('home')  # Replace 'home' with your actual home page name
            else:
                messages.error(request, 'Invalid username or password.')
        except User.DoesNotExist:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'crops/login_user.html')

def season_detail(request, season_id):
    season = get_object_or_404(Season, id=season_id)
    crops = Crop.objects.filter(season=season)
    return render(request, 'crops/season_detail.html', {'season': season, 'crops': crops})

def create_season(request):
    if request.method == 'POST':
        form = SeasonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SeasonForm()
    return render(request, 'crops/season_form.html', {'form': form})

def update_season(request, season_id):
    season = get_object_or_404(Season, id=season_id)
    if request.method == 'POST':
        form = SeasonForm(request.POST, instance=season)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = SeasonForm(instance=season)
    return render(request, 'crops/season_form.html', {'form': form})

def delete_season(request, season_id):
    season = get_object_or_404(Season, id=season_id)
    if request.method == 'POST':
        season.delete()
        return redirect('home')
    return render(request, 'crops/season_confirm_delete.html', {'season': season})

def create_crop(request, season_id):
    season = get_object_or_404(Season, id=season_id)
    if request.method == 'POST':
        form = CropForm(request.POST)
        if form.is_valid():
            crop = form.save(commit=False)
            crop.season = season
            crop.save()
            return redirect('season_detail', season_id=season_id)
    else:
        form = CropForm()
    return render(request, 'crops/crop_form.html', {'form': form, 'season': season})

def update_crop(request, season_id, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    if request.method == 'POST':
        form = CropForm(request.POST, instance=crop)
        if form.is_valid():
            form.save()
            return redirect('season_detail', season_id=season_id)
    else:
        form = CropForm(instance=crop)
    return render(request, 'crops/crop_form.html', {'form': form, 'season': crop.season})

def delete_crop(request, season_id, crop_id):
    crop = get_object_or_404(Crop, id=crop_id)
    if request.method == 'POST':
        crop.delete()
        return redirect('season_detail', season_id=season_id)
    return render(request, 'crops/crop_confirm_delete.html', {'crop': crop})
