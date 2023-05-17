from django.shortcuts import render

# Create your views here.

def app1(request):
    d={'name':'venkydare', 'age':25, 'gender':'Male'}
    return render(request,'app1.html',d)