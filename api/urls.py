from django.urls import path
from .import views

urlpatterns = [
    
    path('students/',views.studentsView,name='studentsView'),
    path('student/<int:pk>/',views.studentDetailView,name='studentDetailView'),
    path('employees/',views.EmployeeView.as_view(),name='EmployeeView'),
    path('employees/<int:pk>/',views.EmployeeDetailView.as_view(),name='EmployeeDetailView'),
]
