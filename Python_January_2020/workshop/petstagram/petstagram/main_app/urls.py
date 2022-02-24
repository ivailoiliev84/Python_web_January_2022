from django.urls import path

from petstagram.main_app.views.generic_views import index, dashboard
from petstagram.main_app.views.pet_photo_views import photo_details, like_pet_photo, create_photo, edit_photo
from petstagram.main_app.views.pet_views import create_pet, edit_pet, delete_pet
from petstagram.main_app.views.profile_views import profile_details, create_profile, edit_profile, delete_profile

"""
Create Profile Page: http://127.0.0.1:8000/profile/create/  
Add Pet Page: http://127.0.0.1:8000/pet/add/  
Pet Edit Page: http://127.0.0.1:8000/pet/edit/<pet_id>/ 
Pet Delete Page: http://127.0.0.1:8000/pet/delete/<pet_id>/ 
Add Photo Page: http://127.0.0.1:8000/photo/add/  
Photo Edit Page: http://127.0.0.1:8000/photo/edit/<photo_id>/ 
Profile Edit Page: http://127.0.0.1:8000/profile/edit/ 
Profile Delete Page: http://127.0.0.1:8000/profile/delete/
"""

urlpatterns = (
    path('', index, name='home'),
    path('dashboard/', dashboard, name='dashboard'),


    path('profile/', profile_details, name='profile details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),


    path('pet/add/', create_pet, name='create pet'),
    path('pet/edit/<int:pk>', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>', delete_pet, name='delete pet'),

    path('photo/add/', create_photo, name='create photo'),
    path('photo/edit/<int:pk>', edit_photo, name='edit photo'),


    path('photo/details/<int:pk>', photo_details, name='photo details'),
    path('photo/like/<int:pk>', like_pet_photo, name='like_photo'),

)
