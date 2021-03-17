from django.urls import path, include
from . import views

app_name = 'job'
urlpatterns = [

    path('signup', views.signup, name = 'signup'),
    path('profile', views.profile_h, name = 'profile'),
    path('profile_edit', views.profile_edit, name = 'profile_edit'),

]
