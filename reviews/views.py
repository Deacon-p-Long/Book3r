# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from reviews.models import Book
from reviews.utils import average_rating



def index (request):
    return render (request, "base.html")



def book_search (request):
    search_query = request.GET.get ("search", "")
    return render (request, "search_results.html", {"search_query": search_query})



def book_list (request):
    books = Book.objects.all()
    book_list = []
    for book in books:
        reviews = book.review_set.all ()
        if reviews:
            rating = average_rating ([review.rating for review in reviews])
            num_reviews = len (reviews)
        else:
            rating = None
            num_reviews = 0
        book_list.append({'book': book,
                          'rating': rating,
                          'num_reviews': num_reviews})
    context = {'book_list': book_list}
    return render (request, "book_list.html", context)