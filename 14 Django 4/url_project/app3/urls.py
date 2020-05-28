from django.urls import path
from app3 import views

app_name = 'app3'
urlpatterns = [
    path('page2/',views.page2, name='page2'),
    path('relate/', views.relate, name='relate')
]
