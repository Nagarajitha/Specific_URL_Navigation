from django.shortcuts import render

# Create your views here.
def dewars(request):
    return render(request, 'dewars.html')
def teachers(request):
    return render(request,'teachers.html')