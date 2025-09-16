from numpy.f2py.crackfortran import include_paths
from django.contrib import admin
from django.urls import include,path
from admin1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.landingpage, name='landingpage'),
    path('login', views.loginpage, name='loginpage'),
    path('register', views.registerpage, name='registerpage'),
    path('users', views.listusers, name='userspage'),
    path('getuser/<int:idx>', views.getuser, name='user'),
    path('delete/<int:idx>', views.deleteuser, name='delete'),
    path('update/<int:idx>', views.update, name='update'),
]