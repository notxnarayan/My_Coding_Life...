from django.shortcuts import redirect,render
from admin1.models import User

def landingpage(request):
    return render(request,'dashboard2.html')

def loginpage(request):
    return render(request,'login.html')

def registerpage(request):
    if request.method=='POST':
        print(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        image=request.FILES.get('image')
        User.objects.create(name=name,email=email,phone=phone,password=password,image=image)
    return render(request,'register.html')

def listusers(request):
    search=request.POST.get('search')
    if search:
        users=User.objects.filter(name=search)
    else:
        users=User.objects.all()
    return render(request,'listusers.html',{'users':users})

def getuser(request,idx):
    user=User.objects.get(id=idx)
    return render(request,'user.html',{'user':user})

def deleteuser(request,idx):
    user=User.objects.get(id=idx)
    user.delete()
    return redirect('userspage')

def update(request,idx):
    user=User.objects.get(id=idx)
    if request.method=='POST':
        print(request.POST)
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        password=request.POST.get('password')
        image=request.FILES.get('image')
        user.name=name
        user.email=email
        user.phone=phone
        user.password=password
        user.image=image
        user.save()
        return redirect('userspage')
    return render(request,'updateuser.html',{'user':user})