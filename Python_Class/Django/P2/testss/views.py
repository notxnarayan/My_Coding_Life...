from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from sqlalchemy.ext.serializer import Serializer

from .models import category
from rest_framework.response import Response
from testss.models import category,Product
from testss.serializers import CategorySerializer,ProductSerializer,ProductSerializer1,ProductSerializer2
from rest_framework.decorators import api_view
from rest_framework import status
def landingpage(request):
    return render(request, "dashboard2.html")

def table(request):
    products = category.objects.all()
    return render(request, 'table.html', {'products': products})

def form(request):
    print(request.POST.get)
    if request.method == 'POST':
        name = request.POST.get('name')
        des = request.POST.get('description')
        image = request.FILES.get('image')
        print("image is", image)
        category.objects.create(categoryname=name, image=image, description=des)
        return render(request, 'dashboard2.html')
    return render(request, 'form.html')

def custom_login(request):
    print("Check")
    if request.method == 'POST':
        print("Check")
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=email,
                            password=password)  # username=email because USERNAME_FIELD = 'email'
        print("Check")
        if user is not None:
            print("Check")
            login(request, user)
            request.session['user_id'] = user.id
            request.session['username'] = user.username
            request.session['email'] = user.email
            request.session['name'] = user.first_name
            request.session['is_superuser'] = user.is_superuser

            # redirect based on role
            if user.is_superuser:
                print("redirecting")
                return redirect('home')  # send to dashboard/home
            else:
                print("redirecting")
                return redirect('home')  # normal users also go to home (or client page if you want)
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    print("redirecting")
    return render(request, 'login.html')

def deletecategory(request,catid):
    cat = category.objects.get(id=catid)
    cat.delete()
    return redirect('table')

def viewcategory(request,catid):
    cat = category.objects.get(id=catid)
    return render(request,'viewcategory.html',{'categories':cat})

def updatecategory(request,catid):
    cat = category.objects.get(id=catid)
    if request.method=='POST':
        name=request.POST.get('name')
        des=request.POST.get('description')
        image = request.FILES.get('image')
        cat.categoryname=name
        cat.description=des
        cat.image=image
        cat.save()
        return redirect('table')
    return render(request,'updatecategory.html',{'category':cat})

@api_view(['GET'])
def listcategoriesapi(request):
    categories = category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)

# @api_view(['POST'])
# def addcategoryapi(request):
#     print("printttt")
#     print(request.POST)
#     if request.method=='POST':
#         name=request.data.get('name')
#         des=request.data.get('description')
#         image = request.FILES.get('image')
#         cat=category.objects.create(categoryname=name,image=image,description=des)
#         return Response(
#             {"message": "Category added successfully", "id": cat.id, "name": cat.categoryname},
#             status=status.HTTP_201_CREATED
#         )
@api_view(['POST'])
def addcategoryapi(request):
    serializer = CategorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors)

@api_view(['DELETE'])
def deletecategoriesapi(request, catid):
    cat = category.objects.get(id=catid)
    cat.delete()
    return Response(
                  {"message": "Category added successfully", "id": cat.id, "name": cat.categoryname},
                  status=status.HTTP_201_CREATED
              )

@api_view(['GET'])
def getuserdataapi(request, catid):
    cat = category.objects.get(id=catid)
    return Response(CategorySerializer(cat, many=False).data)

@api_view(['GET'])
def filtercategoryapi(request):
    #name = request.data.get('name')
    name = request.GET.get('search','')
    print(name)
    cat = category.objects.filter(categoryname__contains=name)
    print(cat)
    return Response(CategorySerializer(cat, many=True).data)

# @api_view(['PUT'])
# def updatecategoryapi(request,id):
#     cate=category.objects.get(id=id)
#     name=request.data.get('categoryname')
#     des=request.data.get('description')
#     image = request.FILES.get('image')
#     cate.categoryname=name
#     cate.description=des
#     cate.image=image
#     cate.save()
#     return Response(
#             {"message": "Category updated successfully"},
#             status=status.HTTP_200_OK
#         )

@api_view(['PUT'])
def updatecategoryapi(request,catid):
    cate=category.objects.get(id=catid)
    serializer = CategorySerializer(cate,data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Category updated successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def listproductsapi(request):
    categories = Product.objects.all()
    serializer = ProductSerializer(categories, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addproductapi(request):
    serializer = ProductSerializer2(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Product created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
