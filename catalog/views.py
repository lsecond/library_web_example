from django.shortcuts import render

from .models import Book, Author, BookInstance, Genre
from django.views import generic


def index(request):
    """
    View function for home page of site.
    """
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    num_books_with_new = Book.objects.filter(title__icontains='new').count()
    num_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # The 'all()' is implied by default.

    num_genres = Genre.objects.all().count()

    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_books_with_new': num_books_with_new,
            'num_visits': num_visits,
        },
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 4
    # context_object_name = 'my_book_list'  # your own name for the list as a template variable
    # queryset = Book.objects.all()[:5]  # Get 5 books containing the title war
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 4


class AuthorDetailView(generic.DetailView):
    model = Author
