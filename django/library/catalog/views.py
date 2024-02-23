from django.shortcuts import render
from transliterate import translit

from catalog.models import Author, Publisher


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

