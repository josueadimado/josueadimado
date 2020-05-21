from django.shortcuts import render, redirect,HttpResponse
import os, binascii
from .models import *
import json
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def index(request):
    template_name = "accounts/index.html"
    args = {}
    return render(request,template_name,args)

@csrf_exempt
def serviceapi(request):
    json_data = json.loads(str(request.body, encoding='utf-8'))
    service = json_data['service']
    message = json_data['message']
    budget = json_data['budget']
    deadline = json_data['deadline']
    email = json_data['email']
    work = Work()
    work.service = service
    work.message = message
    work.budget = budget
    work.deadline = deadline
    work.email = email
    work.save()
    data = {'success':True, 'message':"Thank you for contacting me. I will get back to you soon!"}
    dump = json.dumps(data)
    return HttpResponse(dump, content_type='application/json')