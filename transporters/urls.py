from django.urls import path
from . import views

app_name = "trans"

urlpatterns = [
	path('', views.trans_list, name="index"),
	path('<int:id>/', views.trans_list, name="detail"),	
]