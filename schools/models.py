from django.db import models

# School Class holds Colleges and Universities the user is interested in attending
class School(models.Model):
	name = models.CharField(max_length = 200)
	location = models.CharField(max_length = 200)
	tuition = models.FloatField(default = 0.00)
	visit = models.BooleanField(default = False)
	applied = models.BooleanField(default = False)
	accepted = models.BooleanField(default = False)

	def __str__(self):
		return self.name

# Major Class holds the majors the user has expressed an interest.
class Major(models.Model):
	school = models.ManyToManyField(School, default = 1)
	major_name = models.CharField(max_length=100)
	degree = models.CharField(max_length=10)
	

	def __str__(self):
		return self.major_name + " (" + self.degree + ")"

