from django.shortcuts import render

def index (request):
    return render (request, "base.html")

def book_search (request):
    search_query = request.GET.get ("q")
    return render (request, "search_results.html", {"search_query": search_query})