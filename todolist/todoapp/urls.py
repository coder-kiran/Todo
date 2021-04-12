from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.index,name='home'),
    path('update/<int:commonid>/',views.update,name='update')
    
]