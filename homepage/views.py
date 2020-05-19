from django.shortcuts import render,redirect

# Create your views here.
def homepage_view(request):
	return render(request,'home.html',{})
