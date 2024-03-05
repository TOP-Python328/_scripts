from django import forms
from django.core.exceptions import ValidationError

from re import compile

from catalog.models import Author, Publisher, Book


pat_name = compile(r'(?P<name>[A-Za-zА-ЯЁа-яё]{2,})(-(?P=name))?')


def validate_name(value: str):
    if not pat_name.fullmatch(value):
        raise ValidationError(
            f'{value!r} не является именем',
            params={"value": value}
        )


class AddAuthorForm(forms.Form):
    last_name = forms.CharField(
        label='Фамилия',
        max_length=30,
        validators=[validate_name],
    )
    first_name = forms.CharField(
        label='Имя',
        max_length=30,
        validators=[validate_name],
    )
    
    def is_valid(self):
        is_valid = super().is_valid()
        if is_valid:
            if Author.objects.filter(**self.cleaned_data):
                self.add_error(None, 'такой автор уже существует')
                return False
        return is_valid


class AddPublisherForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = ['name']


class AddExistingBookToPublisherForm(forms.Form):
    book_id = forms.ChoiceField(
        label='Существующая книга',
        choices= {'': ''} | {
            book.id: repr(book)
            for book in Book.objects.order_by('title')
        },
    )


class AddNewBookToPublisherForm(AddAuthorForm):
    title = forms.CharField(
        label='Название',
        max_length=100,
    )
    
    field_order = ['title', 'last_name', 'first_name']
    
    def is_valid(self):
        # return super(self.__class__.__mro__[1], self).is_valid()
        return super(AddAuthorForm, self).is_valid()

