from django.shortcuts import get_object_or_404, render
from .models import Book
from django.db.models import Avg,Max,Min

# Create your views here.
def index(request):
    books=Book.objects.all().order_by("-title")
    num_books=books.count()
    avg_rating=books.aggregate(Avg("rating"))

    return render(request,"book_outlet/index.html",{
        "books":books,
        "total_number_of_books":num_books,
        "avg_rating":avg_rating
    })

def book_detail(request,slug):
    # book=Book.objects.get(pk=id) try/except
    book=get_object_or_404(Book,slug=slug)
    return render(request,"book_outlet/book_detail.html",{
        "title":book.title,
        "author":book.author,
        "is_bestseller":book.is_bestselling,
        "rating":book.rating
    })