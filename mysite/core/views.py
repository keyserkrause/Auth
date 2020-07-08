from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView 
from django.core.files.storage import FileSystemStorage

from .forms import FileForm
from .models import File
# Create your views here.
class Home(TemplateView):
	template_name = 'home.html'

def upload(request):
	context = {}
	if request.method =='POST':
		uploaded_file = request.FILES['document']
		fs = FileSystemStorage()
		name = fs.save(uploaded_file.name, uploaded_file) 
		context['url'] = fs.url(name)	
	return render(request, 'upload.html', context)
	

def file_list(request):
	files = File.objects.all()
	return render(request, 'file_list.html', {
		'files': files
		})

def upload_file(request):
	if request.method == 'POST':
		form = FileForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('file_list')	
	else:
		form = FileForm()
	return render(request, 'upload_file.html',{
		'form':form
		})
		

def home(request):
	count = User.objects.count()
	return render(request, 'home.html', {
		'count':count
		})



def signup(request):
	if request.method == 'POST':
		form = UserCreationForm(request.POST)
		if form.is_valid():
		   form.save()
		   return redirect('home')
	else:
			form = UserCreationForm()
	return render(request, 'registration/signup.html', {
		'form': form
	})