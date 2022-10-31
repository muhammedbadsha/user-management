from . import views
from django.urls import path

urlpatterns = [
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('',views.home,name='home'),
    path('logout/',views.logout,name='logout'),
    

]