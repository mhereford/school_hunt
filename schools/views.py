from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse

from .models import School, Major
from .forms import SchoolForm, MajorForm

def index(request):
	"""Home Page for School Hunt"""
	return render(request, 'schools/index.html')

# FUNCTIONS for the SCHOOL object.
def schools(request):
	"""Display all schools."""
	schools = School.objects.order_by('name')
	context = {'schools':schools}
	return render(request, 'schools/schools.html', context)


def school(request, school_id):
	"""Show detail for a single school identified by school_id."""
	school = School.objects.get(id=school_id)
	majors = school.major_set.order_by('major_name')
	context = {'school':school, 'majors':majors}
	return render(request, 'schools/school_detail.html', context)

def add_school(request):
	"""Add a new school."""
	if request.method != 'POST':
		# If No data submitted; create a blank form.
		form = SchoolForm()
	else:
		# POST data submitted; process data
		form = SchoolForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('schools:schools'))

	context = {'form':form}
	return render(request, 'schools/add_school.html', context)

def update_school(request, school_id):
	"""Update School information."""
	school = School.objects.get(id=school_id)
	majors = school.major_set.order_by('major_name')
	if request.method != 'POST':
		# If No data submitted; create a blank form.
		form = SchoolForm(instance=school)
	else:
		# POST data submitted; process data
		form = SchoolForm(instance=school, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('schools:school', args=[school_id]))

	context = {'school':school, 'form':form}
	return render(request, 'schools/update_school.html', context)

def delete_school(request, school_id):
	"""Delete a school."""
	school = School.objects.get(id=school_id)
	print('School ID '+ school_id )
	if request.method=='GET':
		school.delete()
		print('School Deleted')
		return redirect('schools:schools')
	print('Before Return')
	return render(request, 'schools/confirm_delete.html', {'school':school})



# FUNCTIONS for the MAJOR Object
def majors(request):
	"""Display all majors."""
	majors = Major.objects.order_by('major_name')
	context = {'majors':majors}
	return render(request, 'schools/majors.html', context)

def major(request, major_id):
	"""This is where you will add major to a school"""

	# TODO Include the list of schools for each major 
	
	major = Major.objects.get(id=major_id)
	context = {'major':major}
	return render(request, 'schools/major_detail.html', context)


def add_major(request):
	"""Add a new major."""
	if request.method != 'POST':
		# If No data submitted; create a blank form.
		form = MajorForm()
	else:
		# POST data submitted; process data
		form = MajorForm(data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('schools:majors'))

	context = {'form':form}
	return render(request, 'schools/add_major.html', context)

def update_major(request, major_id):
	"""Update a major."""
	major = Major.objects.get(id=major_id)

	if request.method != 'POST':
		# If No data submitted; create a blank form.
		form = MajorForm(instance=major)
	else:
		# POST data submitted; process data
		form = MajorForm(instance=major, data=request.POST)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect(reverse('schools:major', args=[major_id]))

	context = {'school':school, 'major':major, 'form':form}
	return render(request, 'schools/update_major.html', context)

def delete_major(request, major_id):
	"""Delete a major."""
	major = Major.objects.get(id=major_id)
	if request.method=='GET':
		major.delete()
		return redirect('schools:majors')
	return render(request, 'schools/confirm_delete.html', {'major':major})
