from django.db import models
from django.urls import reverse

class TrasnporterDetails(models.Model):
	name = models.CharField(max_length=250, verbose_name="Transporter Name")
	gst_no = models.CharField(max_length=15, verbose_name="Transporter ID")

	class Meta:		
		ordering = ('name',)
		verbose_name_plural = "Transporter Details"

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse("trans:detail", args=[self.id])