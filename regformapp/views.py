from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from .models import reg

# Create your views here.

class home(View):
    def get(self,request):
        return render(request,'home.html')
class Reginput(View):
    def get(self,request):
        return render(request,templates='regi.html')
class loginput(View):
    def get(self,request):
        return render(request,templates='login.html')
class regview(view):
    def post(self,request):
        fn=request.POST["t1"]
        ln=request.POST["T2"]
        un=request.POST["t3"]
        psw=request.POST["t4"]
        cpsw=request.POST["t5"]
        eml=request.POST["t6"]
        mbl=request.post["t7"]
        r1=reg(first_name=fn,last_name=ln,user_name=un,password=psw,cpassword=cpsw,email=eml,
               mobile=mbl)
        r1.save()
        return  HttpResponse("registaction succes")
class loginview(View):
    def post(self,request):
        un=request.POST["t1"]
        pwd=request.POST["t2"]
        res=reg.objects.filter(useername=un,password=pwd)
        if res:
            return HttpResponse("login success")
        else:
            return HttpResponse("login faild")