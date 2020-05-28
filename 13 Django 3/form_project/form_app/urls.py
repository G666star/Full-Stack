from django.urls import path
from form_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('forms/',views.form_func, name='form')
]
