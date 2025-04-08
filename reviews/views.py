from django.shortcuts import render

def index (request):
    #name = request.GET.get ("name") or "world"
    #return HttpResponse ("Hello {}!" .format (name))
    return render (request, "base.html")
