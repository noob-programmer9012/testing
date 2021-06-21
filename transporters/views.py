from django.shortcuts import render, get_object_or_404
from .models import TrasnporterDetails

def trans_list(request):
	transporters = TrasnporterDetails.objects.all()
	context = {
		'transporters': transporters,
	}
	return render(request, 'transporters/index.html', context)

def trans_detail(request, id):
	transporters = TrasnporterDetails.objects.all()
	transporter = TrasnporterDetails.objects.get(id=id)
	context = {
		'transporters': transporters,
		'transporter': transporter,
	}
	return render(request, 'transporters/index.html', context)