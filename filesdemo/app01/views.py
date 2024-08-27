import os
from django.utils.encoding import escape_uri_path
from django.http import HttpResponse

from app01 import models
from django.shortcuts import render, redirect


def index(request):
    username = request.session.get("username")
    tip = "请选择要上传的文件！"
    if request.method=="POST":
        #上传文件
        myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
        tip="上传文件成功！"
        models.files.objects.create(files_name=myFile,files_user_id=username)
        return render(request, "index.html", {"tip": tip, "username": username})
    return render(request,"index.html",{"tip":tip,"username":username})
# 登陆
def login(request):
    tip="请进行登陆！"
    if request.method == "POST":
        username=request.POST.get("user")
        userpwd=request.POST.get("pwd")
        if username=="" or userpwd=="":
            tip="账号或密码不能为空"
            return render(request,"login.html",{"tip":tip})
        if models.userinfo.objects.filter(user_name=username):
            user = models.userinfo.objects.get(pk=username)
            if userpwd==user.user_pwd:
                request.session['username'] = username
                return redirect("/index/")
            else:
                tip="密码错误！"
                render(request, "login.html", {"tip": tip})
        else:
            tip="账号不存在！"
            render(request, "login.html", {"tip": tip})
    return render(request,"login.html",{"tip":tip})
# 注册
def reg(request):
    tip=""
    if request.method=="POST":
        user=request.POST.get("user")
        pwd=request.POST.get("pwd")
        print(user,pwd)
        if models.userinfo.objects.filter(user_name=user):
            tip="账号已存在！"
            return render(request, "reg.html", {"tip": tip})
        else:
            models.userinfo.objects.create(user_name=user,user_pwd=pwd)
            return redirect("/login")
    return render(request,"reg.html",{"tip":tip})

# 查看所有上传文件
def file(request):
    files_data=models.files.objects.all()
    return render(request,"file_list.html",{"files":files_data})

# 下载文件
def download_view(request):
    photo = request.GET.get('photo', '')
    file = open("static/"+photo, 'rb')
    response = HttpResponse(file)
    response['Content-Type'] = 'application/octet-stream'  # 设置头信息，告诉浏览器这是个文件
    # response['Content-Disposition'] = 'attachment;filename='+photo[6:]
    print(photo[6:])
    # response['Content-Disposition'] = 'attachment;filename={}'.format(photo[6:].encode("utf-8"))
    response['Content-Disposition'] = f'attachment;filename={escape_uri_path(photo[6:])};'
    return response

# Create your views here.
