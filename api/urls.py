from django.urls import path,include
from .import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('employees',views.EmployeeView,basename='employees')


urlpatterns = [
    
    path('students/',views.studentsView,name='studentsView'),
    path('student/<int:pk>/',views.studentDetailView,name='studentDetailView'),
    # path('employees/',views.EmployeeView.as_view(),name='EmployeeView'),
    # path('employees/<int:pk>/',views.EmployeeDetailView.as_view(),name='EmployeeDetailView'),

    
    path('',include(router.urls)),

    path('blogs/',views.BlogsView.as_view(),name='BlogsView'),
    path('comments/',views.CommentsView.as_view(),name='CommentsView'),

    path('blogs/<int:pk>/',views.BlogDetailView.as_view(),name='Blogs'),
    path('comments/<int:pk>/',views.CommentDetailView.as_view(),name='Comments'),

]
