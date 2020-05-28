from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(request):
	return HttpResponse('<h1>Hello Hi!</h1>')
	

def app_index(request):
	dict_mine = {'insert_1': 'now this from temp_app/index.html'}
	return render(request,'temp_app/index.html',context=dict_mine)

def help(request):
	help_dict = {'insert_2': 'help from temp_app/help.html'}
	return render(request,'temp_app/help.html',context=help_dict)