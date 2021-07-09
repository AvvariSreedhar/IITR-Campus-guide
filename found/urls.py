from django.urls import path

from . import views

app_name = 'found'
urlpatterns = [
    path('', views.index, name='index'), 
    path('<int:item_id>/', views.details, name='details'), 
    path('report/', views.report, name='report'), 
]