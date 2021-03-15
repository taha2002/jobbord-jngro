from django.urls import path, include
from . import views

urlpatterns = [

    path('', job_list),
    path('<int:id>', job_list),
]
