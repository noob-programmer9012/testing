from django.shortcuts import render
from .models import TrasnporterDetails

def trans_list(request, id=None):	
	transporters = TrasnporterDetails.objects.all()
	try:
		transporter = TrasnporterDetails.objects.get(pk=id)
		context = {
			'transporters': transporters,
			'transporter': transporter,
		}
		return render(request, 'transporters/index.html', context)
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