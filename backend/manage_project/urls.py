from django.urls import path
from . import views

urlpatterns = [
    path('project_list/', views.TblProjectView.as_view(), name='project_list'),
]