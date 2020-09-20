from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('stu',views.stu),
    path('show',views.show),
    path('delete/<int:id>',views.delete),
    path('Login',views.doLogin),

   
]
