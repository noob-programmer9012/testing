from django.shortcuts import render, get_object_or_404
from .models import TrasnporterDetails
from django.http import HttpResponse

def trans_list(request, id=None):	
	transporters = TrasnporterDetails.objects.all()
	try:
		transporter = TrasnporterDetails.objects.get(pk=id)
		return render(request, 'transporters/index.html', {'transporters': transporters, 'transporter': transporter})
	except:		
		context = {
			'transporters': transporters,			
		}
		return render(request, 'transporters/index.html', context)



# def trans_detail(request, id):
# 	transporters = TrasnporterDetails.objects.all()
# 	transporter = TrasnporterDetails.objects.get(id=id)
# 	context = {
# 		'transporters': transporters,
# 		'transporter': transporter,
# 	}
# 	return render(request, 'transporters/index.html', context)