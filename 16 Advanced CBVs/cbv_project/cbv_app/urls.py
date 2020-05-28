from django.urls import path
from cbv_app import views

app_name = 'cbv'

urlpatterns = [
    path('', views.SkoolListView.as_view(template_name='app5_temp/school_list.html'), name='list'),
     # either define template here or in views.py coz default is something else, check that in debug or or when error occurs or online
     # in course notes urls.py template_name is not defined coz it used default
    path('<int:pk>/', views.SkoolDetailView.as_view(template_name='app5_temp/school_detail.html'), name='detail'),
    path('create/', views.SkoolCreateView.as_view(), name='banao'),
    path('update/<int:pk>/', views.SkoolUpdateView.as_view(template_name='app5_temp/school_create.html'), name='thik'),
    path('delete/<int:pk>/', views.SkoolDelView.as_view(), name='khatam')
]
