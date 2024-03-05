from django.shortcuts import render
from transliterate import translit

from catalog.forms import AddAuthorForm
from catalog.models import Author, Publisher, Book


authors_cache = {
    translit(author.last_name, 'ru', reversed=True).lower(): author
    for author in Author.objects.order_by('last_name', 'first_name')
}
publishers_cache = {
    translit(pub.name, 'ru', reversed=True).lower(): pub
    for pub in Publisher.objects.order_by('name')
}


def main(request):
    return render(
        request,
        'main.html',
    )


def authors(request):
    if request.method == 'GET':
        form = AddAuthorForm()
    
    elif request.method == 'POST':
        form = AddAuthorForm(request.POST)
        if form.is_valid():
            Author(**form.cleaned_data).save()
        # breakpoint()
    
    return render(
        request,
        'authors.html',
        {
            'authors': Author.objects.order_by('last_name', 'first_name'),
            'form': form,
        }
    )


def author(request, name: str):
    author = authors_cache[name]
    return render(
        request, 
        'author.html',
        {
            'author': author,
            'books': author.book_set.all(),
        }
    )


def publishers(request):
    return render(
        request,
        'publishers.html',
        {
            'pubs': Publisher.objects.order_by('name')
        }
    )


def publisher(request, name: str):
    pub = publishers_cache[name]
    return render(
        request,
        'publisher.html',
        {
            'pub': pub,
            'books': pub.books.all()
        }
    )


def add_book(request):
    context = {
        'added': False,
        'authors': Author.objects.all(),
        'double': False,
    }
    
    if request.method == 'POST':
        # print(request.POST)
        title = request.POST['title']
        author_id = int(request.POST['author_id'])
        double = Book.objects.filter(title=title, author_id=author_id)
        # print(double)
        if not double:
            Book(title=title, author_id=author_id).save()
            context['added'] = True
        else:
            context['double'] = True
    
    return render(
        request,
        'add_book.html',
        context
    )

