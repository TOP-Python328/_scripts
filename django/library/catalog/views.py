from django.shortcuts import render
from transliterate import translit

from catalog.models import Author, Publisher, Book


authors = {
    translit(author.last_name, 'ru', reversed=True).lower(): author
    for author in Author.objects.order_by('last_name', 'first_name')
}
publishers = {
    translit(pub.name, 'ru', reversed=True).lower(): pub
    for pub in Publisher.objects.order_by('name')
}


def main(request):
    return render(
        request,
        'main.html',
    )


def author_catalog(request):
    return render(
        request,
        'authors.html',
        {
            'authors': Author.objects.order_by('last_name', 'first_name'),
        }
    )


def author(request, name: str):
    author = authors[name]
    return render(
        request, 
        'author.html',
        {
            'author': author,
            'books': author.book_set.all(),
        }
    )


def pubs(request):
    return render(
        request,
        'publishers.html',
        {
            'pubs': Publisher.objects.order_by('name')
        }
    )


def pub(request, name: str):
    pub = publishers[name]
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

