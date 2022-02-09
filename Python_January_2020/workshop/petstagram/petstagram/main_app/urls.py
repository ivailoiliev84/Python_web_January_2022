from django.urls import path

from petstagram.main_app.views import index, dashboard, profile_details, photo_details, like_pet_photo

urlpatterns = (
    path('', index, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile/', profile_details, name='profile details'),
    path('photo/details/<int:pk>', photo_details, name='photo details'),
    path('photo/like/<int:pk>', like_pet_photo, name='like_photo'),
)
