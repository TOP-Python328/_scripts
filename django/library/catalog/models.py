from django.db import models


class Author(models.Model):
    class Meta:
        db_table = 'authors'
    
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    
    def __repr__(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return f'{self.last_name} {self.first_name}'


class Book(models.Model):
    class Meta:
        db_table = 'books'
    
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    
    def __repr__(self):
        return self.title


class Publisher(models.Model):
    class Meta:
        db_table = 'publishers'
    
    id = models.SmallAutoField(primary_key=True)
    name = models.CharField(max_length=150, unique=True)
    authors = models.ManyToManyField(Author)
    books = models.ManyToManyField(Book)
    
    def __repr__(self):
        return self.name

