from django.shortcuts import render, redirect
from .models import Course
from datetime import datetime

# Create your views here.
def index(req):
	context = {
		'courses': Course.objects.all()
	}
	return render(req, 'new_courses/index.html', context)

def process(req):
	if req.method == 'POST':
		Course.objects.create(name=req.POST['name'], description=req.POST['description'], date_added=datetime.now())
		return redirect ('/')

def delete(req, id):
	# why does the id variable as the 2nd parameter works when you put in urls.py, and how does it know to find it and put in here
	context = {
		"courseid": Course.objects.get(id=id)
	}
	return render(req, 'new_courses/delete.html', context)

def delprocess(req, id):
	Course.objects.filter(id=id).delete()
	return redirect('/')