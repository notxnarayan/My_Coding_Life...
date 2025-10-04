from django.contrib import admin
from django.urls import path
from testss import views

urlpatterns = [
    path("", views.custom_login, name="login"),   # login page
    path("home", views.landingpage, name="home"),
    path("table", views.table, name="table"),
    path("form", views.form, name="form"),
    path("deletecategory/<int:catid>", views.deletecategory, name="deletecategory"),
    path('viewcategory/<int:catid>', views.viewcategory,name='viewcategory'),
    path('updatecategory/<int:catid>', views.updatecategory,name='updatecategory'),
    path('listcategoriesapi', views.listcategoriesapi,name='listcategoriesapi'),
    path('addcategoryapi', views.addcategoryapi,name='addcategorypageapi'),
    path('deletecategoryapi/<int:catid>', views.deletecategoriesapi,name='deletcategoryapi'),
    path('getuserdataapi/<int:catid>', views.getuserdataapi,name='getuserdataapi'),
    path('filtercategoryapi', views.filtercategoryapi, name='filtercategory'),
    path('updatecategoryapi/<int:catid>', views.updatecategoryapi, name='updatecategoryapi'),
    path('listproductsapi', views.listproductsapi, name='listproductsapi'),
    path('addproductapi', views.addproductapi,name='addcategorypageapi'),
]
