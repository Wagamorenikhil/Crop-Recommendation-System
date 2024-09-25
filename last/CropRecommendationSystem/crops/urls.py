from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('season/admin/', views.login_admin, name='login_admin'),
    path('season/user/', views.login_user, name='login_user'),
    path('season/home/', views.home, name='home'),
    path('season/<int:season_id>/', views.season_detail, name='season_detail'),
    path('season/create/', views.create_season, name='create_season'),
    path('season/update/<int:season_id>/', views.update_season, name='update_season'),
    path('season/delete/<int:season_id>/', views.delete_season, name='delete_season'),
    path('season/<int:season_id>/crop/create/', views.create_crop, name='create_crop'),
    path('season/<int:season_id>/crop/update/<int:crop_id>/', views.update_crop, name='update_crop'),
    path('season/<int:season_id>/crop/delete/<int:crop_id>/', views.delete_crop, name='delete_crop'),
]
