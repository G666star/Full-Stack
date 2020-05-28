from django.urls import path
from app_by_me import views

urlpatterns = [
	path('',views.index,name='index'),
	path('temp_index/',views.app_index,name='app_index'),
	path('help/',views.help,name='help'),
]