from django.shortcuts import render

# Create your views here.
def index(request):
    if request.method == 'GET':
        return render(request,'index.html')
    
def reviews(request):
    if request.method == "GET":
        return render(request, "reviews.html")
    

def drivers(request):
    if request.method == "GET":
        return render(request, "drivers.html")