from django.shortcuts import render
from django.http import HttpResponse


def signup_view(request,name,age,last_name):
    x=request.GET.get('your id')
    return HttpResponse(f'Signup Completed! mr {name} {last_name} age= {age}' your id is {x})
