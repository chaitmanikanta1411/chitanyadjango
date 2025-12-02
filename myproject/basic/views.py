from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
# Create your views here.

def sample(request):
    return HttpResponse('puka')
def sample1(request):
    return HttpResponse('welcome to django')
def sampleInfo(request):
    data={"name":"sumanth",'age':25,'city':'hyd'}
    return JsonResponse(data)
 
def dynamicResponse(request):
    name=request.GET.get("name",'kiran')
    city=request.GET.get("city","hyd")
    return HttpResponse(f"erripuka {name} from {city}")