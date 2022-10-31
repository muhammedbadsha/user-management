from  . import views
from django.urls import path

urlpatterns = [
    path('admin_login',views.admin_login,name='admin_login'),
    path('',views.admin_home,name='admin_home'),
    path('admin_logout',views.admin_logout,name='admin_logout'),
    path('viewuser/<int:id>',views.viewuser,name='viewuser'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('adduser',views.adduser,name ='adduser' ),
    path('searchuser',views.searchuser,name = 'searchuser'),
    path('adminupdate/<int:id>',views.adminupdate,name='adminupdate')


]