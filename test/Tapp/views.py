from django.shortcuts import render
from django.http import HttpResponse

def signup_view(request,name,age,last_name):
    return HttpResponse(f'Signup Completed! mr {name} {last_name} age= {age}')
