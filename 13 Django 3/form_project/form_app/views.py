from django.shortcuts import render
from form_app import forms

# Create your views here.

def index(request):
    index_dict = {'here': 'enter /forms for forms list'}
    return render(request, 'form_templates/index.html', context=index_dict)

def form_func(request):
    form1 = forms.UserForm()

    if request.method == 'POST':     # should be 'POST' and not 'post'
        form1 = forms.UserForm(request.POST)
        if form1.is_valid():
            print('kjsdksdn')
            print(form1.cleaned_data['name'])
            print(form1.cleaned_data)
    return render(request, 'form_templates/form_page.html', {'insert5': form1})
