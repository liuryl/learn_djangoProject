from django.http import HttpResponse
from django.shortcuts import render
import datetime
# def hello(request):
#     return HttpResponse("hello word!")

# def runoob(request)://模板用例
#     context ={}
#     context['hello']='hello world!'
#     return render(request,'runoob.html',context)
# 模板标签
# def runoob(request):
#     view_name = "菜鸟"
#     return render(request,'runoob.html', {"name":view_name})
# 列表
# def runoob(request):
#     view_list=["caniao1","cainiao2","cainiao3"]
#     return render(request,"runoob.html",{"view_list":view_list})
# 字典
# def runoob(request):
#     view_dict = {"name":"菜鸟"}
#
#     return render(request,"runoob.html",{"view_dict":view_dict})

# 过滤器
# def runoob(request):
#     name=2048
#     return render(request,"runoob.html",{"name":name})
def runoob(request):
    # now =datetime.datetime.now()
    # return render(request,"runoob.html",{"time":now})
    # 超过规定数量用。。。代替
    # view_str="菜鸟教程"
    # return render(request,"runoob.html",{"view_str":view_str})
    # 内容安全无需转译
    # view_str="<a href='https://www.runoob.com/'>点击跳转</a>"
    # return render(request,"runoob.html",{"view_str":view_str})