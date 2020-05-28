from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Skool, Student

# Create your views here.


class TempView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self,**kwargs):
        context  = super().get_context_data(**kwargs)
        context['injectme'] = "Basic Injection!"
        return context

class SkoolListView(ListView):
    # either define template here or in urls.py coz default is something else, check that in debug or or when error occurs or online
    context_object_name = 'jhinga_list' # default is object_list(skool_list)
    model = Skool # code with tutorials will not match coz import method is different

class SkoolDetailView(DetailView):
    context_object_name = 'jhinga_detail' # default is object(skool)
    model = Skool

class SkoolCreateView(CreateView):
    model = Skool
    fields = '__all__'
    template_name = 'app5_temp/school_create.html'

class SkoolUpdateView(UpdateView):
    model = Skool
    fields = ('Name', 'Dean')

class SkoolDelView(DeleteView):
    model = Skool
    success_url = reverse_lazy('cbv:list')
    context_object_name = 'zenga_del' # default is object(skool)
    template_name = 'app5_temp/school_delete.html'
