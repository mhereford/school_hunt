""" Holds URL Patters for school app"""

from django.conf.urls import url

from . import views

# URL Patterns defined
urlpatterns = [
	# Home Page
	url(r'^$', views.index, name="index"),
	url(r'^schools/$', views.schools, name="schools"),
	url(r'^majors/$', views.majors, name="majors"),

	# School Detail 
	url(r'^schools/(?P<school_id>\d+)/$', views.school, name='school'),
	# Add School Form
	url(r'^add_school/$', views.add_school, name='add_school'),
	# Edit School Form
	url(r'^update_school/(?P<school_id>\d+)/$', views.update_school, name='update_school'),
	# Delete School View
	url(r'^delete_school/(?P<school_id>\d+)/$', views.delete_school, name='delete_school'),
	
	# Major Detail 
	url(r'^majors/(?P<major_id>\d+)/$', views.major, name='major'),
	# Add Major Form
	url(r'^add_major/$', views.add_major, name='add_major'),
	# Edit Major Form
	url(r'^update_major/(?P<major_id>\d+)/$', views.update_major, name='update_major'),
	url(r'^delete_major/(?P<major_id>\d+)/$', views.delete_major, name='delete_major'),
]

