"""forms.py contains the forms for adding and/or editing Schools and Majors"""

from django import forms

from .models import School, Major

class SchoolForm(forms.ModelForm):
	class Meta:
		model = School
		fields = ['name',
				  'location',
				  'tuition',
				  'visit',
				  'applied',
				  'accepted']


class MajorForm(forms.ModelForm):
	class Meta:
		model = Major
		fields = [ 'school',
				   'major_name',
				   'degree']