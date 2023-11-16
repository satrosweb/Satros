from django.urls import path
from . import views


app_name = "projects"

urlpatterns = [
    path('list/', views.ProjectList.as_view(), name="api_projects_list"),
    path('<slug:slug>/<int:pk>/', views.ProjectDetail.as_view(), name="project_detail")
]