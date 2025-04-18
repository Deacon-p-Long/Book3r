from django.http import HttpResponse
from django.shortcuts import render

from reviews.models import Book



def welcome (request):
    message = (f"<html><h1>Welcome to Bookr!</h1>"
               f"<p>{Book.objects.count ()} books and counting!</p></html>")
    return HttpResponse (message)


def index (request):
    return render (request, "base.html")



def book_search (request):
    search_query = request.GET.get ("q")
    return render (request, "search_results.html", {"search_query": search_query})