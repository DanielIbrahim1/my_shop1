
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('adminregister',views.admin_registser , name='adminregister'),
    path('userregister',views.user_registser , name='userregister'),
    path('login',views.MyTokenObtainPairView.as_view(), name='login'),
 
    # path('login',views.MyTokenObtainPairView.as_view(), name='')
    path ('test', views.test , name='test')
]
