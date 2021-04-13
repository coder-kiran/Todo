from django.urls import path
from todoapp import views

urlpatterns = [
    path('',views.index,name='home'),
    path('delete/<int:commonid>',views.deletelist,name='delete'),
    path('update/<int:commonid>/',views.update,name='update')   
]