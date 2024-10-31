<<<<<<< HEAD
from django.shortcuts import render,HttpResponse

def home(request):
    context = {'name':"SAS","course":[x**2 for x in range(10)]}
    # return HttpResponse("This is the index home page(/)")
    return render(request,'home.html',context)

def about(request):
    # return HttpResponse("This is the about page(/)")
    context = {'page':"About","course":"Django"}
    return render(request,'about.html',context)

def project(request):
    context = {'page':"Project","course":"Django"}
    return render(request,'project.html',context)
    # return HttpResponse("This is the projects page(/)")
def contact(request):
    context = {'page':"Contact","course":"Django"}
    return render(request,'contact.html',context)
    # return HttpResponse("This is the contact page(/)")


=======
from django.shortcuts import render,HttpResponse

def home(request):
    context = {'name':"SAS","course":[x**2 for x in range(10)]}
    # return HttpResponse("This is the index home page(/)")
    return render(request,'home.html',context)

def about(request):
    # return HttpResponse("This is the about page(/)")
    context = {'page':"About","course":"Django"}
    return render(request,'about.html',context)

def project(request):
    context = {'page':"Project","course":"Django"}
    return render(request,'project.html',context)
    # return HttpResponse("This is the projects page(/)")
def contact(request):
    context = {'page':"Contact","course":"Django"}
    return render(request,'contact.html',context)
    # return HttpResponse("This is the contact page(/)")


>>>>>>> 71eb6d68001fddf933b81a692248a82e014d8378
