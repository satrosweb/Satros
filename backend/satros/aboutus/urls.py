from django.urls import path
from . import views


app_name = "aboutus"


urlpatterns = [
    path('employe/list/', views.EmployeList.as_view(), name="employe_list"),
    path('employe/detail/', views.EmployeDetail.as_view(), name='employe_detail'),
]