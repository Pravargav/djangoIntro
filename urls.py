from django.urls import path

from . import views

app_name= 'register'

urlpatterns = [
    path('', views.index, name='index'),
      
    path('<int:student_id>/', views.detail, name='detail'),
   
    path('<int:student_id>/results/', views.results, name='results'),
    
    path('<int:student_id>/vote/', views.vote, name='vote'),
]
