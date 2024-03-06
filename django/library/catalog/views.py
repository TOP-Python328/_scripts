from django.shortcuts import render, redirect
from transliterate import translit

from catalog.forms import (
    AddAuthorForm, 
    AddPublisherForm, 
    AddExistingBookToPublisherForm, 
    AddNewBookToPublisherForm
)
from catalog.models import Author, Publisher, Book

from django.contrib.auth.forms import UserCreationForm


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
    if request.method == 'GET':
        form = AddPublisherForm()
    
    elif request.method == 'POST':
        form = AddPublisherForm(request.POST)
        if form.is_valid():
            form.save()
            form = AddPublisherForm()
    
    return render(
        request,
        'publishers.html',
        {
            'pubs': Publisher.objects.order_by('name'),
            'form': form,
        }
    )


def publisher(request, name: str):
    pub = publishers_cache[name]
    
    form1 = AddExistingBookToPublisherForm()
    form2 = AddNewBookToPublisherForm()
    
    if request.method == 'POST':
        if request.POST['form'] == 'existing':
            form1 = AddExistingBookToPublisherForm(request.POST)
            form1.full_clean()
            book = Book.objects.get(pk=form1.cleaned_data['book_id'])
            pub.books.add(book)
            form1 = AddExistingBookToPublisherForm()
        
        elif request.POST['form'] == 'new':
            form2 = AddNewBookToPublisherForm(request.POST)
            if form2.is_valid():
                # дописать самостоятельно создание/получение экземпляров автора и книги
                author = ...
                book = ...
                
                pub.books.add(book)
                form2 = AddNewBookToPublisherForm()
    
    return render(
        request,
        'publisher.html',
        {
            'pub': pub,
            'books': pub.books.all(),
            'form1': form1,
            'form2': form2,
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


def register(request):
    if request.method == 'GET':
        form = UserCreationForm()
    
    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main', permanent=True)
    
    return render(
        request,
        'register.html',
        {'form': form}
    )

