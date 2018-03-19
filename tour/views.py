from django.shortcuts import render
from django.http import HttpResponseRedirect
#from django.contrib.gis.geoip import GeoIP
#from misc.test import "somefunction or class"

# Create your views here.

def index(request):

	if request.method == 'POST':
		days = request.POST['days']
		cities = request.POST['city']
		priority = request.POST['priori']
		print("done")
      	#output = "somefunction or class"(days,cities,priority) 
     	# Here you are calling script_function, 
     	# passing the POST data for 'info' to it;
	    #return render(request, 'tour/output.html',{'output': output,})
	else:
		return render(request, 'tour/index.html')
	return render(request, 'tour/index.html')