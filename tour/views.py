from django.shortcuts import render
from django.http import HttpResponseRedirect
from misc.test import get_plan

# Create your views here.

# def index(request):

# 	if request.method == 'POST':
# 		days = request.POST['days']
# 		cities = request.POST['city']
# 		priority = request.POST['priori']
# 		print("done")
# 		output = test(days,cities,priority)
# 		print (output)
# 		return render(request, 'tour/output.html',{'output': output,})
# 	else:
# 		return render(request, 'tour/index.html')
# 	return render(request, 'tour/index.html')

def index(request):
	days=4
	cities=['jaipur','udaipur','ajmer','alwar','barmer','amer','barmer','jaisalmer','bikaner','mount abu city','pushkar','nathdwara','bhadra city','kota']

	priority=['monument','shrine']
	print('done')
	output = get_plan(days,cities,priority)
	for out in output:
		print(out.city)
		for place in out[out.city]:
			print(place.name+"|"+str(place.lat)+"|"+str(place.lng))
	return render(request, 'tour/output.html',{'output': output,})