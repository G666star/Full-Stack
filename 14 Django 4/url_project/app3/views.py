from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'app3_temp/index.html',)

def page2(request):
    return render(request, 'app3_temp/other.html')

def relate(request):
    return render(request, 'app3_temp/relate.html')
